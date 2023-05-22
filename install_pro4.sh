#!/bin/bash

#Execute only in the PRO4 folder

# Update system
sudo apt-get update
sudo apt-get upgrade -y

# Install prerequisites
sudo apt-get install -y git docker.io python3-pip python3-venv

# Install required packages
pip install --upgrade pip
pip install -r requirements.txt

# Start the application
#python app.py &
#sleep 5

# Dockerization
sudo docker build -t pro4 .
sudo docker run -d -p 5000:5000 --name pro4-container pro4 &
