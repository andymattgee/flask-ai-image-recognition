import os
from dotenv import load_dotenv
import sys

# Get the absolute path to the directory containing this script
script_dir = os.path.dirname(os.path.abspath(__file__))
print(f"Script directory: {script_dir}")

# Path to the .env file
dotenv_path = os.path.join(script_dir, '.env')
print(f"Looking for .env file at: {dotenv_path}")
print(f".env file exists: {os.path.exists(dotenv_path)}")

# Load the .env file
load_dotenv(dotenv_path)

# Check if the API key is loaded
api_key = os.environ.get("OPENAI_API_KEY")
if api_key:
    print(f"API key found: {api_key[:5]}...")
else:
    print("API key not found!")
    print(f"Environment variables: {list(os.environ.keys())}")

print("\nInstructions:")
print("1. Make sure you have a .env file (not .env.example) in the backend directory")
print("2. Make sure the .env file contains: OPENAI_API_KEY=your_actual_api_key_here")
print("3. Restart the Flask server after making changes to the .env file") 