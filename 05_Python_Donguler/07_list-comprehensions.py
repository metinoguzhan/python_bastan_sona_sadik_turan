for x in range(10):
    print(x)

numbers = [x for x in range(10)]
print(numbers)


listNumber = []

for x in range(10, 20):
    listNumber.append(x)
print(listNumber)


for x in range(10):
    print(x**2)


listNum = [x**2 for x in range(10)]
print(listNum)


listNum = [x*x for x in range(60,90) if x % 3 == 0]
print(listNum)


myString = 'Hello'
myList = []

for letter in myString:
    myList.append(letter)
print(myList)


myString = 'Metin'
myList = [letter for letter in myString]
print(myList)

import datetime

years = [1983, 1999, 2008, 1956, 1986]
ages = [
    datetime.datetime.now().year - year  for year in years 
]
print(ages)



results = [
    x if x % 2 == 0 else 'TEK'  for x in range(1,10)
]

print(results)



result = []

for x in range(3):
    for y in range(3):
        result.append((x,y))
print(result)



result = [ (x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(result)
