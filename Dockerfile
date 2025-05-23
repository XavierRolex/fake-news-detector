# 1. Use slim base image
FROM python:3.11-slim

# 2. Working directory
WORKDIR /app

# 3. Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 4. Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# 5. Copy application code
COPY . .

# 6. Environment settings
ENV PYTHONUNBUFFERED=1

# 7. Expose FastAPI port
EXPOSE 8000

# 8. Launch the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
