# Fake News Detector

A Streamlit application that uses Google's Gemini AI to detect fake news and analyze content authenticity.

## Deployment Instructions

### Prerequisites
- A GitHub account
- A Streamlit Cloud account (free)
- Google API key for Gemini AI

### Steps to Deploy

1. **Push your code to GitHub**
   - Create a new repository on GitHub
   - Push your code to the repository
   - Make sure to include:
     - `new.py` (main application file)
     - `requirements.txt`
     - `.env` file (for API keys)

2. **Deploy on Streamlit Cloud**
   - Go to [Streamlit Cloud](https://streamlit.io/cloud)
   - Sign in with your GitHub account
   - Click "New app"
   - Select your repository
   - Set the main file path to `new.py`
   - Add your environment variables:
     - `GOOGLE_API_KEY`: Your Google API key
   - Click "Deploy"

3. **Environment Variables**
   Create a `.env` file with:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

### Local Development
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the app:
   ```bash
   streamlit run new.py
   ```

## Features
- User authentication
- News content analysis
- Trust score calculation
- Fake news probability detection
- Analysis history tracking

# Breifly   

Breifly is a news summarizer that is powered with Streamlit and Gemini. By deafault it loads data from the CSV files includes within this repository. All the data used in this project is taken from BBC.


## Environment Variables

To run this project, you can either enter your Gemini API directly or you can export GEMINI_API_KEY as an env variable and then import it in your code.


## Run Locally

Clone the project

```bash
git clone https://github.com/karanlvm/Gemini-Fake-News.git
```

Go to the project directory

```bash
cd Gemini Fake News
```

Install dependencies

```bash
pip install requirements.txt
```

Run the application

```bash
streamlit run new.py
```

