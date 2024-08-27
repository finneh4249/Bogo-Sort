#!/bin/bash
echo "Installing and verifying dependencies..."

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

clear

echo "Starting Bogo-Sort..."
sleep 1
python3 bogosort.py $1
