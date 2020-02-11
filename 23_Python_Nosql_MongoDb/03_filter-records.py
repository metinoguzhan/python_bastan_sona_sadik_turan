import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient(
    "mongodb+srv://username:[PASSWORD]@cluster0-82uxf.mongodb.net/node-app?retryWrites=true&w=majority"
)


mydb = myclient["node-app"]
mycollection = mydb["products"]

# filters = {
#     "name":"Samsung S5"
# }

# result = mycollection.find_one(filter=filters)
# print(result)

# result = mycollection.find({"name":"Samsung S5"})
# result = mycollection.find_one({"_id":ObjectId("5e31818099842d862ed07c5f"}))

# result = mycollection.find({
#     "name": {
#         "$in" : ["Samsung S5","Samsung S6"]
#     }
# })


# result = mycollection.find({
#     "price":{
#         "$gt": 2000
#     }
# })

#greather then and equals
# result = mycollection.find({
#     "price":{
#         "$gte":3000
#     }
# })

#equal : 
# result = mycollection.find({
#     "price":{
#         '$eq':2000
#     }
# })


# result = mycollection.find({
#     "price" : {
#         '$lte' : 3000
#     }
# })

# S ile başlayan bütün kayıtları getir...
result = mycollection.find({
    "name" : {"$regex":"^S"}
})


for i in result:
    print(i)



