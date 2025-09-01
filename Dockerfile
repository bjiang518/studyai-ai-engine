FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements-railway.txt .
RUN pip install --no-cache-dir -r requirements-railway.txt

# Copy source code
COPY src/ ./src/
COPY .env.example .env

# Run the application (Python will read PORT environment variable)
CMD ["python", "-m", "src.main"]