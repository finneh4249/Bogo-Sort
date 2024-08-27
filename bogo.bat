@echo off
echo Installing and verifying dependencies...
python -m venv venv
call venv\bin\activate.bat
pip install -r requirements.txt

cls

echo Starting Bogo-Sort...
timeout /t 1 /nobreak
python bogosort.py %1

