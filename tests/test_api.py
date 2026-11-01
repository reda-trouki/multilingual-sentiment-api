from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_positive_english():
    response = client.post("/v1/analyze", json={"text": "This is excellent, I love it!"})
    assert response.status_code == 200
    assert response.json()["sentiment"]["label"] == "positive"

def test_negative_french():
    response = client.post("/v1/analyze", json={"text": "C'est mauvais et terrible, je suis déçu."})
    assert response.status_code == 200
    assert response.json()["sentiment"]["label"] == "negative"

def test_darija_flag():
    response = client.post("/v1/analyze", json={"text": "هاد الخدمة زوينة بزاف"})
    assert response.status_code == 200
    assert response.json()["darija_detected"] is True

def test_batch():
    response = client.post("/v1/analyze/batch", json={"texts": ["I love it", "This is bad"]})
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_blank_rejected():
    response = client.post("/v1/analyze", json={"text": "   "})
    assert response.status_code == 422
