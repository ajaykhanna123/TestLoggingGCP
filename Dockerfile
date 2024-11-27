# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Run tests when building the image (optional step)
RUN python -m unittest discover tests || echo "Tests failed"

# Define the command to run the app
CMD ["python", "app.py"]
