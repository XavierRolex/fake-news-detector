
# 📰 Fake News Detector API
> Detect fake news in seconds with a robust ML ensemble model—lightning-fast predictions, reliably hosted on Railway.


[![codecov](https://codecov.io/gh/XavierRolex/fake-news-detector/graph/badge.svg?token=W9F9WTOONT)](https://codecov.io/gh/XavierRolex/fake-news-detector)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110.2-009688?logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Model: scikit-learn](https://img.shields.io/badge/Model-scikit--learn-orange)
[![Hosted on Railway](https://img.shields.io/badge/Deployed%20on-Railway-4B5563?logo=railway)](https://fake-news-detector-co.up.railway.app)
[![Try it now](https://img.shields.io/badge/Swagger-Try%20Now-green?logo=swagger)](https://fake-news-detector-co.up.railway.app/docs)


A production‑ready **FastAPI** microservice that predicts whether a news article is **Fake** or **Real** using an ensemble ML model (TF‑IDF + VotingClassifier). Fully Dockerised, CI‑ready, and live on Railway.

---

## 📑 Table of Contents
1. [Features](#features)
2. [Live Demo](#live-demo)
3. [Tech Stack](#tech-stack)
4. [Project Structure](#project-structure)
5. [Local Setup](#local-setup)
6. [Docker Usage](#docker-usage)
7. [API Reference](#api-reference)
8. [Testing](#testing)
9. [Environment Variables](#environment-variables)
10. [License](#license)
11. [Author](#author)
12. [Contributing](#contributing)

---

## ✨ Features
- 🧠 **Ensemble ML pipeline** (TF‑IDF + VotingClassifier)
- ⚡ **FastAPI** backend with automatic Swagger UI (`/docs`)
- 🐳 **Docker‑first** design — build once, run anywhere
- 🧵 **CI/CD ready** with GitHub Actions and automated Codecov reports
- 🛡️ Typed request/response models & custom exception handling
- 🌐 **CORS** enabled for easy front‑end integration

---

## 🚀 Live Demo

> **Base URL:** [`https://fake-news-detector-co.up.railway.app`](https://fake-news-detector-co.up.railway.app)

```bash
$ curl https://fake-news-detector-co.up.railway.app/
{"message":"Fake News Detector API is up and running."}
```

Open [`/docs`](https://fake-news-detector-co.up.railway.app/docs) for an interactive Swagger UI.

<img src="https://github.com/user-attachments/assets/84d19e3b-f298-4a7c-98cf-a101cf33e424" width="800" alt="Swagger UI Screenshot" />
<img src="https://github.com/user-attachments/assets/48541b6e-d19a-4fa6-ae1e-3f66f3b6f198" width="800" alt="Swagger UI Screenshot" />
<img src="https://github.com/user-attachments/assets/662d7766-31de-4373-9a18-32804a303bbb" width="800" alt="Swagger UI Screenshot" />

Use the Swagger interface to test endpoints, send JSON payloads, and view real-time predictions

---

## ⚙️ Tech Stack
- **FastAPI** & **Uvicorn**
- **scikit‑learn** & **joblib**
- **Python 3.11**
- **Docker** & **Railway**
- **Pytest** + **Codecov**

---

## 📁 Project Structure
```text
.
├── app/
│   ├── main.py              # FastAPI entry‑point
│   ├── predictor.py         # Prediction logic
│   ├── logging_config.py    # Centralised logger
│   ├── exceptions.py        # Custom exceptions
│   ├── schemas.py           # Pydantic models
│   └── utils/
│       └── loader.py        # Load model & vectorizer
├── models/
│   ├── ensemble_voting_model.pkl
│   └── tfidf_vectorizer.pkl
├── tests/                   # Unit & integration tests
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── .github/                 # CI workflow
└── README.md
```

---

## 🔧 Local Setup
```bash
# 1. Clone
git clone https://github.com/XavierRolex/fake-news-detector.git
cd fake-news-detector

# 2. (Optional) Create & activate virtual env
python -m venv venv && source venv/bin/activate

# 3. Install deps
pip install -r requirements.txt

# 4. Create a .env file (see below)
echo "MODEL_PATH=models/ensemble_voting_model.pkl" >> .env
echo "VECTORIZER_PATH=models/tfidf_vectorizer.pkl" >> .env

# 5. Run the API
uvicorn app.main:app --reload
```

Visit `http://127.0.0.1:8000/docs` for Swagger UI.

---

## 🐳 Docker Usage
```bash
# Build image
docker build -t fake-news-api .

# Run container
docker run -p 8000:8000 fake-news-api
```

---

## 📡 API Reference

### `GET /`
Health check  
**Response**
```json
{ "message": "Fake News Detector API is up and running." }
```

### `POST /predict`
Predict if text is *Fake* or *Real*  
**Request**
```json
{ "text": "NASA confirms water on the Moon's surface." }
```
**Response**
```json
{ "label": "Fake", "probability": 0.1099 }
```

---

## 🧪 Testing
```bash
pytest --cov=app
```
Coverage reports are uploaded automatically to Codecov via GitHub Actions.

---

## 📄 Environment Variables
| Key | Description | Default |
|-----|-------------|---------|
| `MODEL_PATH` | Path to the trained model | `models/ensemble_voting_model.pkl` |
| `VECTORIZER_PATH` | Path to TF‑IDF vectorizer | `models/tfidf_vectorizer.pkl` |
| `LOG_LEVEL` | Logging level | `INFO` |

> **Note:** On Railway, these are configured via the *Variables* tab.

---

## 📝 License
Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.

---

## 👤 Author
**Nafis Anzum**  
- ✉️ xavier.rolex@icloud.com  
- 🔗 [github.com/XavierRolex](https://github.com/XavierRolex)
- 💼 [LinkedIn](www.linkedin.com/in/xavier-rolex)

---

## 🌟 Contributing
Contributions are welcome! Please open an issue first to discuss your ideas, or submit a pull request.

---

© 2025 Nafis Anzum – All rights reserved.

