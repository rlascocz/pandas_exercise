# Use a minimal Python image as the base image
FROM python:3.9-slim-buster

# Update the package list and install Git
RUN apt-get update 
RUN apt-get install -y git   

# Check Git version
RUN git --version

# Set the working directory inside the container
WORKDIR /app

# Copy your Python application code to the container
COPY . .
VOLUME /app

# Update pip package
RUN pip install --upgrade pip

# Install any required Python packages (specify them in requirements.txt)
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

#docker buildx build -t img_dev .
#docker run -v <folder path>:/app -itd img_dev


