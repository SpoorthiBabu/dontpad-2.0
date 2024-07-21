from pymongo import MongoClient

try:
    client = MongoClient('mongodb://localhost:27017/')
    db = client.test_database
    print("Connection successful!")
except Exception as e:
    print(f"Connection failed: {e}")
