from pymongo import MongoClient
client = MongoClient("localhost",27017) #connects to mongodb compass
db = client.HybridCryptography # connect to db
if db:
    print('Connection Established')
else:
    print("Connection Failed")

# it upload this folder to github for future reference
