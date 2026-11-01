# Transparent baseline lexicons. Extend these with reviewed, native-speaker examples.
LEXICONS = {
    "positive": {
        "en": ["good", "great", "excellent", "love", "amazing", "happy", "perfect", "helpful", "thanks", "thank you"],
        "fr": ["bien", "bon", "bonne", "excellent", "super", "aime", "adore", "génial", "parfait", "merci", "heureux"],
        "ar": ["جيد", "جيدة", "ممتاز", "رائع", "جميل", "زوين", "مزيان", "شكرا", "أحب", "فرحان", "بزاف"],
        "ary": ["زوين", "مزيان", "شكرا", "بغيت", "واخا", "لاباس", "زوينة", "هايل"],
        "es": ["bueno", "buena", "excelente", "genial", "amor", "gracias", "feliz"],
        "de": ["gut", "super", "ausgezeichnet", "liebe", "danke", "glücklich"],
    },
    "negative": {
        "en": ["bad", "terrible", "awful", "hate", "angry", "broken", "worst", "slow", "disappointed", "problem"],
        "fr": ["mauvais", "mauvaise", "terrible", "nul", "déteste", "lent", "problème", "déçu", "déçue", "horrible"],
        "ar": ["سيئ", "سيئة", "خايب", "خايبة", "أكره", "غاضب", "مشكلة", "بطيء", "كارثة", "حزين"],
        "ary": ["خايب", "خايبة", "عييت", "ماشي مزيان", "مشكل", "حشومة"],
        "es": ["malo", "mala", "terrible", "odio", "problema", "lento", "horrible"],
        "de": ["schlecht", "schlimm", "hasse", "problem", "langsam", "enttäuscht"],
    }
}
EMOTIONS = {
    "joy": {
        "en": ["happy", "love", "excited", "wonderful", "great", "amazing", "joy"],
        "fr": ["heureux", "heureuse", "joie", "content", "contente", "ravi", "ravi"],
        "ar": ["فرحان", "سعيد", "فرحة", "مبسوط", "زوين", "مزيان"],
        "ary": ["فرحان", "مزيان", "زوين", "لاباس", "فرحة"],
    },
    "anger": {
        "en": ["angry", "furious", "hate", "annoyed", "useless"],
        "fr": ["colère", "énervé", "énervée", "furieux", "déteste"],
        "ar": ["غاضب", "غضبان", "أكره", "مقلق"],
        "ary": ["مقلق", "عييت", "حشومة"],
    },
    "sadness": {
        "en": ["sad", "unhappy", "disappointed", "lonely", "depressed"],
        "fr": ["triste", "déçu", "déçue", "malheureux"],
        "ar": ["حزين", "حزينة", "مكتئب"],
        "ary": ["حزين", "مقلق"],
    },
    "fear": {
        "en": ["afraid", "scared", "worried", "fear"],
        "fr": ["peur", "inquiet", "inquiète", "effrayé"],
        "ar": ["خائف", "خايف", "قلق"],
        "ary": ["خايف", "قلقان"],
    },
    "surprise": {
        "en": ["wow", "surprised", "unexpected", "amazed"],
        "fr": ["surpris", "surprise", "incroyable"],
        "ar": ["مفاجأة", "مندهش"],
        "ary": ["واو"],
    },
}
