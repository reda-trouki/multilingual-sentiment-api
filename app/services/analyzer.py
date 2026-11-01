import re
from app.services.language import detect_language
from app.services.lexicons import LEXICONS, EMOTIONS

SPAM_TERMS = {
    "en": ["click here", "free money", "claim your prize", "winner", "act now", "buy now", "limited offer"],
    "fr": ["cliquez ici", "argent gratuit", "vous avez gagné", "gagnant", "offre limitée", "achetez maintenant"],
    "ar": ["اربح مجانا", "اضغط هنا", "جائزة", "ربحت", "عرض محدود"],
}
URL_RE = re.compile(r"https?://|www\.", re.I)
REPEATED_RE = re.compile(r"(.)\1{5,}")
MANY_CAPS_RE = re.compile(r"[A-Z]{8,}")

def _count_hits(text: str, terms: list[str]) -> int:
    lowered = text.lower()
    return sum(lowered.count(term.lower()) for term in terms)

def _sentiment(text: str, lang: str):
    # For non-Darija Arabic, use Arabic + Darija terms as a practical baseline.
    keys = [lang, "ar"] if lang in ("ary", "ar") else [lang]
    positive = sum(_count_hits(text, LEXICONS["positive"].get(k, [])) for k in keys)
    negative = sum(_count_hits(text, LEXICONS["negative"].get(k, [])) for k in keys)
    scores = {"positive": 0.0, "negative": 0.0, "neutral": 0.0}
    total = positive + negative
    if total == 0:
        scores["neutral"] = 1.0
    elif positive > negative:
        scores["positive"] = round(0.55 + 0.4 * (positive - negative) / max(total, 1), 3)
        scores["negative"] = round(1 - scores["positive"], 3)
    elif negative > positive:
        scores["negative"] = round(0.55 + 0.4 * (negative - positive) / max(total, 1), 3)
        scores["positive"] = round(1 - scores["negative"], 3)
    else:
        scores = {"positive": 0.25, "negative": 0.25, "neutral": 0.5}
    label = max(scores, key=scores.get)
    return {"label": label, "confidence": scores[label], "scores": scores}

def _emotion(text: str, lang: str):
    keys = [lang, "ar"] if lang in ("ary", "ar") else [lang]
    hits = {}
    for emotion, languages in EMOTIONS.items():
        hits[emotion] = sum(_count_hits(text, languages.get(k, [])) for k in keys)
    if not any(hits.values()):
        return {"label": "neutral", "confidence": 0.65, "scores": {"neutral": 0.65}}
    total = sum(hits.values())
    scores = {k: round(v / total, 3) for k, v in hits.items() if v}
    label = max(scores, key=scores.get)
    return {"label": label, "confidence": scores[label], "scores": scores}

def _spam(text: str, lang: str):
    reasons = []
    keys = [lang, "ar"] if lang in ("ary", "ar") else [lang]
    terms = [term for key in keys for term in SPAM_TERMS.get(key, [])]
    term_hits = _count_hits(text, terms)
    if term_hits:
        reasons.append("Contains common promotional or spam phrases")
    if len(URL_RE.findall(text)) >= 2:
        reasons.append("Contains multiple URLs")
    if REPEATED_RE.search(text):
        reasons.append("Contains excessive repeated characters")
    if len(MANY_CAPS_RE.findall(text)) >= 2:
        reasons.append("Contains multiple all-caps sequences")
    confidence = min(0.99, 0.45 + 0.18 * len(reasons) + 0.08 * term_hits) if reasons else 0.05
    return {"is_spam": bool(reasons), "confidence": round(confidence, 3), "reasons": reasons}

def analyze_text(text: str):
    if not text or not text.strip():
        raise ValueError("Text cannot be empty")
    if len(text) > 5000:
        raise ValueError("Text cannot exceed 5000 characters")
    language, language_name, language_confidence, darija = detect_language(text)
    warnings = [
        "Sentiment and emotion use transparent baseline lexicons; results are not a substitute for a trained production model."
    ]
    if darija:
        warnings.append("Moroccan Darija detection and lexicon coverage are experimental; spelling and dialect variation may reduce accuracy.")
    if language not in ("en", "fr", "ar", "ary", "es", "de"):
        warnings.append("This language has limited lexicon coverage; neutral may mean unsupported vocabulary.")
    return {
        "language": language,
        "language_name": language_name,
        "language_confidence": language_confidence,
        "sentiment": _sentiment(text, language),
        "emotion": _emotion(text, language),
        "spam": _spam(text, language),
        "darija_detected": darija,
        "analysis_mode": "lexicon-baseline",
        "warnings": warnings,
    }
