import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Read from environment variables
api_key = os.environ.get('API_KEY')
database = os.environ.get('DATABASE_URL')

print(f"API Key: {api_key}")
print(f"Using database: {database}")