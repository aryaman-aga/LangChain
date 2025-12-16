import os
from dotenv import load_dotenv

# Load environment variables from a local .env file if present
load_dotenv()

# Read the API key from environment; avoid hardcoding secrets in source control
groq_key = os.getenv("GROQ_API_KEY", "")
