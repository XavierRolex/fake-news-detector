import joblib
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def load_vectorizer():
    vectorizer_path = os.getenv("VECTORIZER_PATH", "models/tfidf_vectorizer.pkl")
    if not os.path.exists(vectorizer_path):
        raise FileNotFoundError(f"Vectorizer not found at {vectorizer_path}")
    return joblib.load(vectorizer_path)

def load_model():
    model_path = os.getenv("MODEL_PATH", "models/ensemble_voting_model.pkl")
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model not found at {model_path}")
    return joblib.load(model_path)
