from http.server import BaseHTTPRequestHandler
import subprocess
import os
import sys

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        message = "Streamlit app is running at the ROOT_URL"
        self.wfile.write(message.encode())
        return

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write('{"status": "ok"}'.encode())
        return

def run_streamlit():
    try:
        # Add the path to the requirements file
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", 
            "-r", "requirements-vercel.txt"
        ])
        
        # Run the Streamlit app
        subprocess.check_call([
            sys.executable, "-m", "streamlit", "run", 
            "new.py", "--server.port=8501", "--server.headless=true"
        ])
    except Exception as e:
        print(f"Error starting Streamlit: {str(e)}")

# Start Streamlit in a separate process when deployed
if os.environ.get('VERCEL_ENV') == 'production':
    import threading
    threading.Thread(target=run_streamlit).start() 