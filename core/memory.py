from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.kiko
memory_col = db.memory

def remember(question, answer):
    memory_col.insert_one({"q": question, "a": answer})

def recall():
    return list(memory_col.find())
