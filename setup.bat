@echo off
echo Setting up environment for Fake News Detector

REM Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Python is not installed or not in PATH
    echo Please install Python 3.8 or later
    exit /b 1
)

REM Install required system packages
echo Installing setuptools and wheel...
pip install --upgrade pip setuptools wheel

REM Create virtual environment if it doesn't exist
if not exist .venv (
    echo Creating virtual environment...
    python -m venv .venv
)

REM Activate virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate

REM Install dependencies
echo Installing dependencies...
pip install --upgrade pip
pip install setuptools wheel

REM Install numpy and pandas separately with binary option
echo Installing numpy and pandas (pre-built binaries)...
pip install --only-binary=:all: numpy==1.24.3
pip install --only-binary=:all: pandas==2.0.3

REM Install other requirements
echo Installing other requirements...
pip install streamlit==1.32.0 google-generativeai==0.3.2 python-dotenv==1.0.1 pymongo==4.6.2 dnspython==2.5.0 gunicorn==21.2.0

echo Setup complete!
echo Run the application with: streamlit run new.py

REM Keep the window open
cmd /k 