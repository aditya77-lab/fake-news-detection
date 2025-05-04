@echo off
echo Setting up environment for Fake News Detector

REM Check Python version
python --version

REM Create virtual environment if it doesn't exist
if not exist .venv (
    echo Creating virtual environment...
    python -m venv .venv
)

REM Activate virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install minimal dependencies
echo Installing minimal dependencies...
pip install -r requirements-minimal.txt

REM Create a .env file template if it doesn't exist
if not exist .env (
    echo Creating .env file template...
    echo GEMINI_API_KEY=your_gemini_api_key_here > .env
    echo MONGODB_URI=your_mongodb_connection_string_here >> .env
    echo Please edit the .env file with your actual API keys
)

echo Setup complete!
echo Run the application with: streamlit run new.py

pause 