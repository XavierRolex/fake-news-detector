import os
import pytest
from unittest import mock
from pathlib import Path
from app.utils import loader


def test_load_vectorizer_env_variable(monkeypatch):
    custom_path = "models/tfidf_vectorizer.pkl"
    monkeypatch.setenv("VECTORIZER_PATH", custom_path)

    with mock.patch("joblib.load") as mock_load:
        mock_load.return_value = "mock_vectorizer"
        result = loader.load_vectorizer()
        mock_load.assert_called_once_with(custom_path)
        assert result == "mock_vectorizer"


def test_load_vectorizer_fallback(monkeypatch):
    monkeypatch.delenv("VECTORIZER_PATH", raising=False)
    fallback_path = "models/tfidf_vectorizer.pkl"

    with mock.patch("joblib.load") as mock_load:
        mock_load.return_value = "mock_vectorizer"
        result = loader.load_vectorizer()
        mock_load.assert_called_once_with(fallback_path)
        assert result == "mock_vectorizer"


def test_load_model_env_variable(monkeypatch):
    custom_path = "models/ensemble_voting_model.pkl"
    monkeypatch.setenv("MODEL_PATH", custom_path)

    with mock.patch("joblib.load") as mock_load:
        mock_load.return_value = "mock_model"
        result = loader.load_model()
        mock_load.assert_called_once_with(custom_path)
        assert result == "mock_model"


def test_load_model_fallback(monkeypatch):
    monkeypatch.delenv("MODEL_PATH", raising=False)
    fallback_path = "models/ensemble_voting_model.pkl"

    with mock.patch("joblib.load") as mock_load:
        mock_load.return_value = "mock_model"
        result = loader.load_model()
        mock_load.assert_called_once_with(fallback_path)
        assert result == "mock_model"


def test_model_file_not_found(monkeypatch):
    monkeypatch.setenv("MODEL_PATH", "nonexistent.pkl")

    # Patch Path.exists to always return False
    monkeypatch.setattr(Path, "exists", lambda self: False)

    with pytest.raises(FileNotFoundError, match="Model not found at nonexistent.pkl"):
        loader.load_model()


def test_vectorizer_file_not_found(monkeypatch):
    monkeypatch.setenv("VECTORIZER_PATH", "nonexistent.pkl")

    # Patch Path.exists to always return False
    monkeypatch.setattr(Path, "exists", lambda self: False)

    with pytest.raises(FileNotFoundError, match="Vectorizer not found at nonexistent.pkl"):
        loader.load_vectorizer()
