fruit = {
    'orange','apple','banana'
}

print(fruit)
# print(fruit[0])    INDEKSLENEMEZ...


for x in fruit:
    print(x)


fruit.add('cherry')
print(fruit)


fruit.update(['grape','mango','apple'])
print(fruit)


fruit.remove('mango')
fruit.discard('apple')
print(fruit)

fruit.pop()
print(fruit)

myList = [1,2,5,4,4,2,1]
print(set(myList))
print(myList)


fruit.clear()