import joblib
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# full paths from .env, or use defaults
MODEL_PATH = os.getenv("MODEL_PATH", "models/ensemble_voting_model.pkl")
VECTORIZER_PATH = os.getenv("VECTORIZER_PATH", "models/tfidf_vectorizer.pkl")

def load_vectorizer():
    if not os.path.exists(VECTORIZER_PATH):
        raise FileNotFoundError(f"Vectorizer not found at {VECTORIZER_PATH}")
    return joblib.load(VECTORIZER_PATH)

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model not found at {MODEL_PATH}")
    return joblib.load(MODEL_PATH)
