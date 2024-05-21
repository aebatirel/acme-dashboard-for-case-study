from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get MongoDB URI from environment variable
mongo_uri = os.getenv('DATABASE_URL')

client = AsyncIOMotorClient(mongo_uri)
database = client.sample_restaurants
