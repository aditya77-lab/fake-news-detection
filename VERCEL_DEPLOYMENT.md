# Deploying to Vercel

This guide explains how to deploy your Fake News Detection application to Vercel.

## Prerequisites

1. A Vercel account (sign up at [vercel.com](https://vercel.com) if you don't have one)
2. Git repository with your code (GitHub, GitLab, or Bitbucket)
3. Your Gemini API key
4. Your MongoDB connection string

## Deployment Steps

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

1. Leave all other settings as default
2. Click "Deploy"

### 5. Check Deployment Status

Vercel will build and deploy your application. Once complete, you'll get a deployment URL (e.g., `your-app-name.vercel.app`).

## Troubleshooting

If your deployment fails:

1. Check the build logs in Vercel to identify the error
2. Make sure all environment variables are correctly set
3. Verify that your MongoDB instance allows connections from Vercel's IP addresses
4. Ensure your Gemini API key is valid and has proper permissions

## Limitations

Note that Streamlit apps on Vercel may have some limitations:

- Streamlit is primarily designed for data apps and may not be optimized for serverless environments
- If you need persistent sessions or heavy computation, consider a platform specifically designed for Streamlit like Streamlit Cloud or Heroku

For production deployments with high traffic, consider using a dedicated Streamlit hosting service. 