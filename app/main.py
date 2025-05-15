from fastapi import FastAPI
from app.schemas import NewsInput, PredictionResult
from app.predictor import predict

app = FastAPI(
    title="Fake News Detector API",
    description="API for detecting fake news using a trained ensemble model.",
    version="1.0.0"
)

@app.get("/", tags=["Health"])
def health_check():
    return {"message": "Fake News Detector API is up and running."}

@app.post("/predict", response_model=PredictionResult)
def predict_news(data: NewsInput):
    return predict(data.text)
