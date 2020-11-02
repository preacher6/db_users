from pymongo import MongoClient

client = MongoClient('localhost')

print(client.list_database_names())