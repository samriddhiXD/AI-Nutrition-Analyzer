import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# USDA API Key
USDA_API_KEY = os.getenv("USDA_API_KEY")

# Database
DATABASE_NAME = "database.db"