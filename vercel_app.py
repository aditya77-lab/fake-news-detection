import streamlit as st
import subprocess
import sys
import os

def run_app():
    # Print environment for debugging
    print("Starting Streamlit app...")
    
    try:
        # Run the main app
        subprocess.check_call([sys.executable, "-m", "streamlit", "run", "new.py", 
                              "--server.port=8501", 
                              "--server.headless=true",
                              "--browser.serverAddress=0.0.0.0"])
    except Exception as e:
        print(f"Error running Streamlit: {str(e)}")
        return {"error": str(e)}
    
    return {"status": "running"}

if __name__ == "__main__":
    run_app() 