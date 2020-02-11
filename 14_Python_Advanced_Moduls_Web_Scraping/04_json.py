import json

person_string = '{"name":"Ali","languages":["Python","C#","Java"]}'
person_dict = {
    "name":"Ali",
    "languages":["Python","C#","Java"]
}

# result = person["name"]
# print(result)


# result = person["languages"]
# print(result)

# result = person["languages"]
# print(result[1])


#********************** JSON string to dict
# result = json.loads(person_string)
# print(type(result))
# print(result)
# print(result['languages'][1])

# with open("14_Python_Advanced_Moduls_Web Scraping/data/person.json") as file:
#     data = json.load(file)
#     print(data)
#     print(data['name'])
#     print(data['languages'])





# => Dic to Json string
# result = json.dumps(person_dict)
# print(result)
# print(type(result))

# with open("14_Python_Advanced_Moduls_Web Scraping/data/person.json","w") as file:
#     json.dump(person_dict,file)

person_dict = json.loads(person_string)
result = json.dumps(person_dict,indent=4,sort_keys=True)
print(person_dict)
print(result)

