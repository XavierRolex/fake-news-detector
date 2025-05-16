import re
import os
from app.logging_config import setup_logger
from app.utils.loader import load_model, load_vectorizer
from app.exceptions import InvalidTextException

logger = setup_logger(__name__)

# Load model and vectorizer once
logger.info("Loading model and vectorizer...")
model = load_model()
vectorizer = load_vectorizer()
logger.info("Model and vectorizer loaded successfully.")

# Text Cleaning Function
def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'<.*?>', '', text)  # remove HTML tags
    text = re.sub(r'https?://\S+|www\.\S+', '', text)  # remove URLs
    text = re.sub(r'[^\w\s]', '', text)  # remove punctuation
    text = re.sub(r'\d+', '', text)  # remove digits
    text = re.sub(r'\s+', ' ', text).strip()  # remove extra spaces
    return text

# Predict Function
def predict(text):
    logger.info("Received prediction request.")
    cleaned_text = clean_text(text)
    logger.debug(f"Cleaned Text: {cleaned_text}")

    if not cleaned_text:
        raise InvalidTextException("Input text is empty after cleaning.")
    if len(cleaned_text) < 10:
        raise InvalidTextException("Input text is too short for prediction.")
    if len(cleaned_text) > 5000:
        raise InvalidTextException("Input text is too long for prediction.")

    logger.info("Transforming text using vectorizer.")
    vectorized_text = vectorizer.transform([cleaned_text])
    prediction = model.predict(vectorized_text)[0]
    logger.info(f"Prediction made: {prediction}")

    probability = (model.predict_proba(vectorized_text)[0][1]
                   if hasattr(model, 'predict_proba') else None)
    label = 'Real' if prediction == 1 else 'Fake'
    return {
        'label': label,
        'probability': round(probability, 4) if probability is not None else 'N/A'
    }
