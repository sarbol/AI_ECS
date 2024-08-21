# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy source code
COPY src/ /app/src
COPY config/ /app/config

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "src/app/main.py"]
