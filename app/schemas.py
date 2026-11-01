from pydantic import BaseModel, Field, field_validator
from typing import Literal

class AnalyzeRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=5000, examples=["هاد الخدمة زوينة بزاف!"])

    @field_validator("text")
    @classmethod
    def text_must_not_be_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("text must not be blank")
        return value

class BatchAnalyzeRequest(BaseModel):
    texts: list[str] = Field(..., min_length=1, max_length=20)

    @field_validator("texts")
    @classmethod
    def validate_texts(cls, values):
        if any(not text.strip() or len(text) > 5000 for text in values):
            raise ValueError("Each text must contain 1–5000 non-whitespace characters")
        return values

class SentimentResult(BaseModel):
    label: Literal["positive", "negative", "neutral"]
    confidence: float
    scores: dict[str, float]

class EmotionResult(BaseModel):
    label: str
    confidence: float
    scores: dict[str, float]

class SpamResult(BaseModel):
    is_spam: bool
    confidence: float
    reasons: list[str]

class AnalyzeResponse(BaseModel):
    language: str
    language_name: str
    language_confidence: float
    sentiment: SentimentResult
    emotion: EmotionResult
    spam: SpamResult
    darija_detected: bool
    analysis_mode: str
    warnings: list[str]
