# Multilingual Sentiment Analysis API

A Python-based REST API built with **FastAPI** that provides multilingual text analysis, including sentiment classification, emotion detection, language identification, and spam detection.

## Features

- **Sentiment Analysis:** Classifies text as positive, negative, or neutral.
- **Emotion Detection:** Identifies emotions such as joy, anger, sadness, fear, and surprise.
- **Language Detection:** Detects the language of submitted text.
- **Darija Support:** Experimental support for Moroccan Arabic and Arabizi.
- **Spam Detection:** Identifies potentially suspicious or spam messages.
- **Batch Analysis:** Analyze multiple texts in a single request.
- **Interactive Documentation:** Explore endpoints through Swagger UI.

## Tech Stack

- Python 3.12
- FastAPI
- Pydantic
- Uvicorn
- Langdetect
- Pytest
- Docker

## Project Status

**Version:** 1.0.0  
**Status:** Beta

V1 uses a lightweight lexicon-based analysis approach and heuristic rules. Advanced machine-learning models and improved language coverage are planned for future releases.

## Getting Started

See the [installation and usage instructions](README.md).

## License

MIT