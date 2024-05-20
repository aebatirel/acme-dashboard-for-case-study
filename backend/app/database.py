from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient('mongodb+srv://semihascioglu:JMik0V8RaeuCTtDG@cluster0.v9jbzhd.mongodb.net/')
database = client.sample_restaurants
