#!/bin/bash
echo "Building Docker image..."
docker-compose down
docker-compose build
docker-compose up -d

echo "Application is deployed and running."
