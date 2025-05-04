# Deploying to Vercel

This guide explains how to deploy your Fake News Detection application to Vercel. Note that while this will work, Streamlit is best deployed on platforms designed for it, like Streamlit Cloud.

## Important Notice

**Streamlit applications are not ideal for Vercel's serverless architecture.** The current setup creates a simple landing page that redirects to a proper Streamlit deployment.

## Better Alternative: Streamlit Cloud

For the best experience, deploy this app on [Streamlit Cloud](https://streamlit.io/cloud) instead:
1. Push your code to GitHub
2. Sign up for Streamlit Cloud (free tier available)
3. Connect your repository
4. Set your secrets (GEMINI_API_KEY, MONGODB_URI)
5. Deploy

## Vercel Deployment Steps

If you still want to proceed with Vercel deployment:

### 1. Push your code to GitHub

Make sure all your code is committed and pushed to your GitHub repository.

### 2. Connect to Vercel

1. Log in to your Vercel account
2. Click "Add New" > "Project"
3. Import your GitHub repository
4. Select the repository containing your Fake News Detection app

### 3. Configure Environment Variables

In the Vercel project settings, add these environment variables:

- `GEMINI_API_KEY`: Your Google Gemini API key
- `MONGODB_URI`: Your MongoDB connection string

### 4. Deploy

1. Make sure the Build Command is set to `pip install -r requirements-vercel.txt`
2. Set the Output Directory to `public` (create an empty public directory if needed)
3. Click "Deploy"

### 5. Check Deployment Status

Vercel will build and deploy your application. The deployed page will redirect users to your Streamlit Cloud deployment.

## Troubleshooting

If your deployment fails:

1. Check the build logs in Vercel to identify the error
2. Make sure all environment variables are correctly set
3. Try downgrading Python packages in requirements-vercel.txt
4. Consider using an older Python version in runtime.txt (3.9 is recommended)
5. If all else fails, deploy directly to Streamlit Cloud instead

## Making Streamlit Work on Vercel (Advanced)

For a true Streamlit deployment on Vercel:
1. Create a Docker-based deployment with a custom Dockerfile
2. Use Vercel's serverless functions to proxy requests to a container
3. Handle session management and state persistence separately

This is complex and not recommended for most use cases. 