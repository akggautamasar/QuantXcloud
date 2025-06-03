# Use the official Python base image
FROM python:3.11.7-slim AS base

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Expose the default port
EXPOSE 8000

# Run the FastAPI application using uvicorn server
CMD ["sh", "-c", "python -m uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]
