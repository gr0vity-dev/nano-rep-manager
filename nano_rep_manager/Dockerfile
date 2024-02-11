FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libffi-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt requirements.txt
RUN pip install wheel
RUN pip install -r requirements.txt

# Copy application files
COPY . .

CMD ["hypercorn", "app:app", "--bind", "0.0.0.0:5000"]

