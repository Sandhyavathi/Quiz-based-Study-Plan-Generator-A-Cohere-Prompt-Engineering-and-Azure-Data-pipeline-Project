# Use a specific Python base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to install dependencies
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app directory into the container
COPY ./app /app

# Ensure the questions.json file is copied into the correct directory inside the container
COPY ./app/quiz_backend/questions.json /app/quiz_backend/questions.json


# Set the environment variable for FastAPI
ENV PYTHONUNBUFFERED=1

# Set the PYTHONPATH to /app so Python can find the 'app' directory
ENV PYTHONPATH=/app

# Expose port 80
EXPOSE 80

# Set the command to run the FastAPI app with Uvicorn
CMD ["uvicorn", "quiz_backend.main:app", "--host", "0.0.0.0", "--port", "80"]

