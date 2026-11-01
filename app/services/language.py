import re
from langdetect import detect, detect_langs, LangDetectException

ARABIC_RE = re.compile(r"[\u0600-\u06FF]")
LATIN_RE = re.compile(r"[A-Za-zÀ-ÿ]")
DARIJA_MARKERS = {
    "واخا", "بزاف", "مزيان", "زوين", "خايب", "شنو", "علاش", "فين",
    "دابا", "غادي", "بغيت", "ماشي", "ديال", "راه", "صافي", "عييت",
    "wach", "bzaaf", "bzaf", "mzyan", "zwina", "khayb", "chno",
    "3lach", "fin", " daba", "ghadi", "bghit", "machi", "dyal",
    "safi", "labas", "hamdullah", "lah"
}
LANG_NAMES = {
    "ar": "Arabic", "fr": "French", "en": "English", "es": "Spanish",
    "de": "German", "it": "Italian", "pt": "Portuguese", "nl": "Dutch",
    "tr": "Turkish", "ru": "Russian", "zh-cn": "Chinese", "ja": "Japanese",
    "unknown": "Unknown"
}

def detect_language(text: str):
    tokens = set(re.findall(r"\w+", text.lower()))
    darija_hits = len(tokens.intersection(DARIJA_MARKERS))
    has_arabic = bool(ARABIC_RE.search(text))
    darija = darija_hits > 0 or (has_arabic and any(x in text for x in ["بزاف", "واخا", "ديال", "دابا", "شنو"]))
    try:
        langs = detect_langs(text)
        top = langs[0]
        code, confidence = top.lang, float(top.prob)
    except (LangDetectException, IndexError):
        code, confidence = "unknown", 0.0

    # Preserve Arabic as the language family while exposing Darija separately.
    if darija:
        code = "ar" if has_arabic else "ary"
        confidence = max(confidence, min(0.99, 0.55 + darija_hits * 0.08))
    name = "Moroccan Darija (experimental)" if darija else LANG_NAMES.get(code, code.upper())
    return code, name, round(confidence, 3), darija
