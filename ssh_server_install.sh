#!/bin/bash

# Update package list
sudo apt update

# Install OpenSSH server
sudo apt install -y openssh-server

# Start and enable the OpenSSH server
sudo systemctl start ssh
sudo systemctl enable ssh

# Optional: Customize SSH server configuration
# For example, you can change the default port and disable password authentication
# Uncomment and modify the following lines as needed
# sudo sed -i 's/#Port 22/Port 2222/' /etc/ssh/sshd_config
# sudo sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config

# Restart the SSH server to apply any configuration changes
sudo systemctl restart ssh

echo "SSH server installed and configured successfully."
