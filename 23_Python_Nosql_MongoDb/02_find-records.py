import pymongo


myclient = pymongo.MongoClient(
    "mongodb+srv://username:[PASSWORD]@cluster0-82uxf.mongodb.net/node-app?retryWrites=true&w=majority"
)


mydb = myclient["node-app"]
mycollection = mydb["products"]


# tek kayıt seçmek için find_one

'''
result = mycollection.find_one()
print(result)
'''



# çoklu kayıt seçmek için find

'''
for i in mycollection.find():
    print(i)
'''
'''
for i in mycollection.find({},{"_id":0,"name":1,"price":1}):
    print(i)
'''
'''
for i in mycollection.find({},{"_id":0}):
    print(i)
'''

'''
for i in mycollection.find({},{"_id":0,"name":0}):
    print(i)
'''
'''
for i in mycollection.find({},{"name":1}):
    print(i)
'''