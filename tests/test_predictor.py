import pytest
from unittest.mock import MagicMock, patch
from app.predictor import predict, clean_text
from app.exceptions import InvalidTextException

# --- Text Cleaning ---
def test_clean_text():
    raw = "Check this out! <b>www.example.com</b> 123 😊"
    expected = "check this out"
    assert clean_text(raw).startswith(expected)

# --- Input Validation Exceptions ---
def test_predict_with_empty_text():
    with pytest.raises(InvalidTextException, match="empty after cleaning"):
        predict("  ")

def test_predict_with_short_text():
    with pytest.raises(InvalidTextException, match="too short"):
        predict("Too short")

def test_predict_with_long_text():
    long_text = "a" * 6000
    with pytest.raises(InvalidTextException, match="too long"):
        predict(long_text)

# --- Valid Prediction (Real Model) ---
def test_predict_with_valid_text():
    result = predict("Vaccines are effective and save lives.")
    assert isinstance(result, dict)
    assert result["label"] in ["Fake", "Real"]
    assert isinstance(result["probability"], (float, str))

# --- Valid Prediction (Mocked) ---
@patch("app.predictor.vectorizer")
@patch("app.predictor.model")
def test_valid_prediction_mocked(mock_model, mock_vectorizer):
    mock_vectorizer.transform.return_value = "mock_vector"
    mock_model.predict.return_value = [1]
    mock_model.predict_proba.return_value = [[0.3, 0.7]]

    response = predict("This is a real news article about the economy.")
    assert response["label"] == "Real"
    assert response["probability"] == 0.7
