from pymongo import MongoClient
import json


client = MongoClient("mongodb://localhost")

print(client)

db = client.book
