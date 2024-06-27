#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Update package lists
echo "Updating package lists..."
sudo apt-get update

# Install Python3 and pip
echo "Installing Python3 and pip..."
sudo apt-get install -y python3 python3-pip

# Install virtualenv if not already installed
echo "Installing virtualenv..."
pip3 install virtualenv

# Create a virtual environment
echo "Creating a virtual environment..."
python3 -m venv venv

# Activate the virtual environment
echo "Activating the virtual environment..."
source venv/bin/activate

# Install required Python packages
echo "Installing required Python packages..."
pip install -r requirements.txt

echo "Setup completed successfully!"
