FROM python:3.11-slim
WORKDIR /app

# Install system dependencies (minimal)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# App and model
COPY app ./app
COPY model ./model

ENV PYTHONUNBUFFERED=1

# Hugging Face Spaces provides PORT env (default 7860)
EXPOSE 7860

# Start the FastAPI app; bind to $PORT
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-7860}"]
