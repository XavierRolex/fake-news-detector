# ───────────────────────────────────────────────────────────────
# Dockerfile for Fake-News-Detector – FastAPI + ML model
# ───────────────────────────────────────────────────────────────

# 1. Base image
FROM python:3.11-slim

# 2. Working directory
WORKDIR /app

# 3. System packages required for building wheels (e.g. wordcloud)
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        libpng-dev \
        libjpeg-dev \
        libfreetype6-dev \
        pkg-config \
    && rm -rf /var/lib/apt/lists/*

# 4. Copy requirements first (leverages Docker layer cache)
COPY requirements.txt .

# 5. Install Python deps
RUN pip install --upgrade pip \
 && pip install --default-timeout=100 --no-cache-dir -r requirements.txt

# 6. Copy the rest of the project
COPY . .

# 7. Environment
ENV PYTHONUNBUFFERED=1

# 8. Expose FastAPI port
EXPOSE 8000

# 9. Launch the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
