# Use an official Python runtime as the base image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages
RUN pip3 install --no-cache-dir -r requirements.txt

# Specify the command to run when the container starts
CMD ["python3", "calculator.py"]
