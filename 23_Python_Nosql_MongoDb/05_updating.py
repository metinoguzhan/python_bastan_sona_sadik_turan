import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient(
    "mongodb+srv://username:[PASSWORD]@cluster0-82uxf.mongodb.net/node-app?retryWrites=true&w=majority"
)

mydb = myclient["node-app"]
mycollection = mydb["products"]



# update_one
# mycollection.update_one(
#     {'name': 'Samsung S6'},
#     {'$set':{
#         'name':'Iphone 7',
#         'price':7777
#     }}
# )

# for i in mycollection.find():
#     print(i)

# update_many
# mycollection.update_many(
#     {'name': 'Samsung S6'},
#     {'$set':{
#         'name':'Iphone 7',
#         'price':7777
#     }}
# )
query = {'name': 'Iphone 9'}
newvalues = {'$set':{
        'name':'Samsung S8',
        'price':2222
}}

result = mycollection.update_many(
    query,
    newvalues
)

print(f"{result.modified_count} adet kayıt güncellendi.")
for i in mycollection.find():
    print(i)