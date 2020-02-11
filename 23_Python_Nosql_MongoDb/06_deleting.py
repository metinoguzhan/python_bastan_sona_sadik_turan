import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient(
    "mongodb+srv://username:[PASSWORD]@cluster0-82uxf.mongodb.net/node-app?retryWrites=true&w=majority"
)

mydb = myclient["node-app"]
mycollection = mydb["products"]


#delete_one()
'''
for i in mycollection.find():
    print(i)

print("*"*50)

mycollection.delete_one({"name" : "Samsung S10"})

for i in mycollection.find():
    print(i)
'''
#delete_many()
for i in mycollection.find():
    print(i)

print("*"*50)
# result = mycollection.delete_many({"name":{"$regex":"^S"}})
# result = mycollection.delete_many({})
result = mycollection.delete_many({"name":"Iphone 8"})
print(f"{result.deleted_count} tane kayıt silindi..")


for i in mycollection.find():
    print(i)
