import pymongo

# myclient = pymongo.MongoClient(
#     "mongodb://localhost:27017"
# )
myclient = pymongo.MongoClient(
    "mongodb+srv://username:[PASSWORD]@cluster0-82uxf.mongodb.net/node-app?retryWrites=true&w=majority"
)


mydb = myclient["node-app"]
mycollection = mydb["products"]

# print(mydb.list_collection_names())

'''
product = {
    "name":"Samsung S5",
    "price":2000
}
result = mycollection.insert_one(product)
print(result)
print(type(result))
print(result.inserted_id)
'''

'''
productList = [
    {"_id":1,"name":"Samsung S6","price":3000},
    {"_id":2,"name":"Samsung S7","price":4000},
    {"_id":3,"name":"Samsung S8","price":5000},
    {"_id":4,"name":"Samsung S9","price":6000},
    {"_id":5,"name":"Samsung S10","price":7000},
    {"_id":6,"name":"Samsung S11","price":8000}
]
'''

'''
productList = [
    {"name":"Samsung S6","price":3000,"description":"iyi telefon"},
    {"name":"Samsung S7","price":4000,"categories":["telefon","elektronik"]},
]

result = mycollection.insert_many(productList)
print(result.inserted_ids)
'''


