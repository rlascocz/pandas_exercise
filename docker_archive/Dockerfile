# Use the official Python image as the base image
FROM python:3.9-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy your Python application code to the container
COPY . .

# Install any required Python packages
RUN pip install -r requirements.txt

# Define the command to run your Python application
CMD ["python", "your_app.py"]
