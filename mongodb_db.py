import os
import pymongo
from datetime import datetime
from dotenv import load_dotenv
import streamlit as st

# Load environment variables
load_dotenv()

# Get MongoDB connection string from environment variables or Streamlit secrets
def get_mongo_uri():
    # Try to get from environment variables first
    mongo_uri = os.getenv("MONGODB_URI")
    
    # If not found, try getting from Streamlit secrets
    if not mongo_uri and hasattr(st, "secrets") and "MONGODB_URI" in st.secrets:
        mongo_uri = st.secrets["MONGODB_URI"]
    
    if not mongo_uri:
        raise Exception("MongoDB URI not found in environment variables or Streamlit secrets")
    
    return mongo_uri

# Initialize MongoDB connection
def init_db():
    try:
        mongo_uri = get_mongo_uri()
        client = pymongo.MongoClient(mongo_uri)
        
        # Create or get the database
        db = client.fake_news_detector
        
        # Create collections if they don't exist
        if "users" not in db.list_collection_names():
            db.create_collection("users")
            # Create unique index on username and email
            db.users.create_index([("username", pymongo.ASCENDING)], unique=True)
            db.users.create_index([("email", pymongo.ASCENDING)], unique=True)
        
        if "analysis_history" not in db.list_collection_names():
            db.create_collection("analysis_history")
        
        # Ping the database to verify connection
        client.admin.command('ping')
        print("Connected to MongoDB successfully")
        
        return db
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        raise e

# Get database instance (singleton pattern)
def get_db():
    if not hasattr(get_db, "db"):
        get_db.db = init_db()
    return get_db.db

# User registration
def register_user(username, password, email):
    try:
        db = get_db()
        
        # Create new user document
        new_user = {
            "username": username,
            "password": password,  # In production, you should hash this password
            "email": email,
            "created_at": datetime.now()
        }
        
        # Insert user document
        result = db.users.insert_one(new_user)
        
        return bool(result.inserted_id)
    except pymongo.errors.DuplicateKeyError:
        # Username or email already exists
        return False
    except Exception as e:
        print(f"Error registering user: {e}")
        return False

# User verification
def verify_user(username, password):
    try:
        db = get_db()
        
        # Find user with matching username and password
        user = db.users.find_one({
            "username": username,
            "password": password  # In production, you should verify the hashed password
        })
        
        if user:
            # Return a tuple similar to the original SQLite function
            return (str(user["_id"]), user["username"], user["email"])
        
        return None
    except Exception as e:
        print(f"Error verifying user: {e}")
        return None

# Save analysis
def save_analysis(user_id, content, result, trust_score, fake_probability):
    try:
        db = get_db()
        
        # Create analysis document
        analysis = {
            "user_id": user_id,
            "content": content,
            "result": result,
            "trust_score": trust_score,
            "fake_probability": fake_probability,
            "date": datetime.now()
        }
        
        # Insert analysis document
        result = db.analysis_history.insert_one(analysis)
        
        return bool(result.inserted_id)
    except Exception as e:
        print(f"Error saving analysis: {e}")
        return False

# Get user history
def get_user_history(user_id):
    try:
        db = get_db()
        
        # Find all analyses for the user
        analyses = db.analysis_history.find({"user_id": user_id}).sort("date", pymongo.DESCENDING)
        
        # Convert to list of tuples similar to the original SQLite function
        history = []
        for analysis in analyses:
            history.append((
                analysis["content"],
                analysis["result"],
                analysis["trust_score"],
                analysis["fake_probability"],
                analysis["date"].strftime("%Y-%m-%d %H:%M:%S")
            ))
        
        return history
    except Exception as e:
        print(f"Error getting user history: {e}")
        return []

# Delete analysis
def delete_analysis(user_id, date):
    try:
        db = get_db()
        
        # Parse the date string to datetime object
        date_obj = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        
        # Delete the analysis
        result = db.analysis_history.delete_one({
            "user_id": user_id,
            "date": {
                "$gte": date_obj.replace(microsecond=0),
                "$lt": date_obj.replace(microsecond=999999)
            }
        })
        
        return bool(result.deleted_count)
    except Exception as e:
        print(f"Error deleting analysis: {e}")
        return False 