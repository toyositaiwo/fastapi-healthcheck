#!/bin/bash

# Change to correct project directory
cd /home/ubuntu/fastapi-healthcheck || exit

# Pull latest code
git pull origin main

# Restart FastAPI service with sudo
sudo systemctl restart fastapi

echo "Deployment complete."
