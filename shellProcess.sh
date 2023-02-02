#!/bin/bash

## Compile the application
echo "Compiling the application..."
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

# Containerize the application
echo "Building the docker image of the application..."
docker build -t calculator .

# Upload the image to the repository
echo "Uploading the image to the repository..."
docker tag calculator rgupta87/mycalculator:latest
docker push rgupta87/mycalculator:latest

# Connect to kubernetes cluster
echo "Connecting to kubernetes cluster..."
kubectl config use-context docker-desktop

# Deploy the application to Kubernetes
echo "Deploying the application to Kubernetes..."
kubectl apply -f deployment_aws.yaml

# Restart the deployment
echo "Waiting for the deployment to complete..."
kubectl rollout status deployment/calculator

echo "Application deployed successfully!"
