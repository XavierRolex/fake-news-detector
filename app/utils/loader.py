import joblib
import os

MODEL_DIR = "models"

def load_vectorizer():
    path = os.path.join(MODEL_DIR, "tfidf_vectorizer.pkl")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Vectorizer not found at {path}")
    return joblib.load(path)

def load_model(model_name="ensemble_voting_model.pkl"):
    path = os.path.join(MODEL_DIR, model_name)
    if not os.path.exists(path):
        raise FileNotFoundError(f"Model not found at {path}")
    return joblib.load(path)