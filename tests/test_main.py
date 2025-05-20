from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Fake News Detector API is up and running."}

def test_predict_valid_text():
    payload = {"text": "The president announced a new policy today."}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "label" in response.json()
    assert "probability" in response.json()

def test_predict_empty_text():
    payload = {"text": ""}
    response = client.post("/predict", json=payload)
    assert response.status_code == 422  # Handled by FastAPI for required fields

def test_predict_short_text():
    payload = {"text": "Hi"}
    response = client.post("/predict", json=payload)
    assert response.status_code == 422
    assert response.json()["error"] == "Input text is too short for prediction."
