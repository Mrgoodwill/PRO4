#!/bin/bash

# Update system
sudo apt-get update
sudo apt-get upgrade -y

# Install prerequisites
sudo apt-get install -y git docker.io python3-pip python3-venv

# Clone repository
git clone https://github.com/VladimirFogel/PRO4.git

# Navigate to the cloned directory
cd PRO4

# Install required packages
pip install --upgrade pip
pip install -r requirements.txt

# Start the application
#python app.py &
#sleep 5

# Dockerization
sudo docker build -t pro4 .
sudo docker run -d -p 5000:5000 --name pro4-container pro4 &
