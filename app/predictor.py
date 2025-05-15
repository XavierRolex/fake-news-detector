import joblib
import re
import string
import os
from app.logging_config import setup_logger
from app.utils.loader import load_model, load_vectorizer

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
        logger.error("Empty text after cleaning.")
        return {"error": "Input text is empty after cleaning."}
    if len(cleaned_text) < 10:
        logger.error("Text too short for prediction.")
        return {"error": "Input text is too short for prediction."}
    if len(cleaned_text) > 5000:
        logger.error("Text too long for prediction.")
        return {"error": "Input text is too long for prediction."}
    logger.info("Transforming text using vectorizer.")

    # Transform the cleaned text using the vectorizer
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
'''
# For Testing Locally
if __name__ == '__main__':
    sample_text = "SAO PAULO (Reuters) - Cesar Mata Pires, the owner and co-founder of Brazilian engineering conglomerate OAS SA, one of the largest companies involved in Brazil s corruption scandal, died on Tuesday. He was 68. Mata Pires died of a heart attack while taking a morning walk in an upscale district of S o Paulo, where OAS is based, a person with direct knowledge of the matter said. Efforts to contact his family were unsuccessful. OAS declined to comment. The son of a wealthy cattle rancher in the northeastern state of Bahia, Mata Pires  links to politicians were central to the expansion of OAS, which became Brazil s No. 4 builder earlier this decade, people familiar with his career told Reuters last year. His big break came when he befriended Antonio Carlos Magalh es, a popular politician who was Bahia governor several times, and eventually married his daughter Tereza. Brazilians joked that OAS stood for  Obras Arranjadas pelo Sogro  - or  Work Arranged by the Father-In-Law.   After years of steady growth triggered by a flurry of massive government contracts, OAS was ensnared in Operation Car Wash which unearthed an illegal contracting ring between state firms and builders. The ensuing scandal helped topple former Brazilian President Dilma Rousseff last year. Trained as an engineer, Mata Pires founded OAS with two colleagues in 1976 to do sub-contracting work for larger rival Odebrecht SA - the biggest of the builders involved in the probe.  Before the scandal, Forbes magazine estimated Mata Pires  fortune at $1.6 billion. He dropped off the magazine s billionaire list in 2015, months after OAS sought bankruptcy protection after the Car Wash scandal. While Mata Pires was never accused of wrongdoing in the investigations, creditors demanded he and his family stay away from the builder s day-to-day operations, people directly involved in the negotiations told Reuters at the time. He is survived by his wife and his two sons."
    result = predict(sample_text)
    print(f"Prediction: {result['label']} (Confidence: {result['probability']})")

# The above code is a complete FastAPI application that includes a predictor module for fake news detection.
# It loads a pre-trained model and vectorizer, cleans the input text, and makes predictions.
'''