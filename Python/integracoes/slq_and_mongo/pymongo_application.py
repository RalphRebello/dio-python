from datetime import datetime

import pymongo


# python -m pip install "pymongo[srv]
# mongodb://pymongo:<db_password>@<hostname>/?ssl=true&replicaSet=atlas-8x70bb-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0

client = pymongo.MongoClient("mongodb+srv://pymongo:pymongo@cluster0.qjmfc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.test
collection = db.test_collection
print(db.list_collection)

# inserir dados
post = {
    "author":"Mike",
    "text":"first mongodb application with python",
    "tags":["mongodb", "python3", "pymongo"],
    "date":datetime.now()
}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)
