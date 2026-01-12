
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import urllib.parse

username = urllib.parse.quote_plus("smartwork")
password = urllib.parse.quote_plus("sm@rt12345")


uri = f"mongodb+srv://{username}:{password}@mywork.dqie7j9.mongodb.net/?appName=mywork"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client["mine_database"]
collection = db["products"]
operation = db["user"]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)