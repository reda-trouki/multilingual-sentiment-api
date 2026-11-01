from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import AnalyzeRequest, AnalyzeResponse, BatchAnalyzeRequest
from app.services.analyzer import analyze_text

app = FastAPI(
    title="Multilingual Sentiment Analysis API",
    description=(
        "Analyze sentiment, emotions, language and spam indicators in multilingual text. "
        "Arabic and Moroccan Darija support is experimental."
    ),
    version="1.0.0",
    contact={"name": "API Support"}
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.get("/", tags=["System"])
def root():
    return {
        "name": "Multilingual Sentiment Analysis API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health",
    }

@app.get("/health", tags=["System"])
def health():
    return {"status": "ok"}

@app.post("/v1/analyze", response_model=AnalyzeResponse, tags=["Analysis"])
def analyze(request: AnalyzeRequest):
    try:
        return analyze_text(request.text)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))

@app.post("/v1/analyze/batch", response_model=list[AnalyzeResponse], tags=["Analysis"])
def analyze_batch(request: BatchAnalyzeRequest):
    try:
        return [analyze_text(text) for text in request.texts]
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))
