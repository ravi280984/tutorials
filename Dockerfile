FROM python:3.11-slim

# Create app directory
WORKDIR /app

# Install system dependencies for some ML libs (kept minimal)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
 && rm -rf /var/lib/apt/lists/*

# Copy and install python deps
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy repo
COPY . /app

# Default command (start a simple uvicorn server if app provides one)
ENV PYTHONUNBUFFERED=1
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
