name = "Metin"
surname = "Oğuzhan"
age = 33
greeting = "My name is " + name + ' ' + surname + ' and \nI am ' + str(age) + " years old."


print("My name is " + name + ' ' + surname + ' and \nI am ' + str(age) + " years old.")
print(greeting)
length = len(greeting)

print(name[0])
print(name[1])
print(name[2])
print(name[-2])
print(name[-1])
print(len(greeting))

print(greeting[length-4])
print(greeting[length-3])
print(greeting[length-2])
print(greeting[length-1])


print(greeting[3:7])
print(greeting[3:])
print(greeting[:10])
print(greeting[2:40:2])  #2 den başla 40 a kadar al ama karakterleri 2 şer olarak al yani : Metin : Mtn
