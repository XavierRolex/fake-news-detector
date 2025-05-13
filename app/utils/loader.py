import joblib
import os

MODEL_DIR = "models"

def load_vectorizer():
    return joblib.load(os.path.join(MODEL_DIR, "tfidf_vectorizer.pkl"))

def load_model(model_name="ensemble_voting_model.pkl"):
    return joblib.load(os.path.join(MODEL_DIR, model_name))