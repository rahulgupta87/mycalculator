#!/bin/bash

# Compile the application
echo "Compiling the application..."
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

# # Run the tests
# echo "Running tests..."
# python -m unittest discover

# Containerize the application
echo "Containerizing the application..."
docker build -t calculator .

# Upload the image to the repository
echo "Uploading the image to the repository..."
docker images
docker tag calculator rgupta87/mycalculator:latest
docker push rgupta87/mycalculator:latest

kubectl config use-context docker-desktop

# Deploy the application to Kubernetes
echo "Deploying the application to Kubernetes..."
kubectl apply -f deployment.yaml

# Wait for the deployment to complete
echo "Waiting for the deployment to complete..."
kubectl rollout status deployment/calculator

echo "Application deployed successfully!"
