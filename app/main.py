from fastapi import FastAPI
from app.schemas import NewsInput, PredictionResult
from app.predictor import predict
from fastapi.middleware.cors import CORSMiddleware
from app.exceptions import (
    InvalidTextException,
    invalid_text_exception_handler,
    generic_exception_handler,
)

app = FastAPI(
    title="Fake News Detector API",
    description="API for detecting fake news using a trained ensemble model.",
    version="1.0.0"
)

# Register Exception Handlers
app.add_exception_handler(InvalidTextException, invalid_text_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Health"])
def health_check():
    return {"message": "Fake News Detector API is up and running."}

@app.post("/predict", response_model=PredictionResult)
def predict_news(data: NewsInput):
    return predict(data.text)
