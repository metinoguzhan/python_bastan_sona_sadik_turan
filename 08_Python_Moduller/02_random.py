import random 

# result = dir(random)
# print(result)


# result = help(random)
# print(result)


# result = random.random()   # 0.0  -  1.0
# print(result)


# result = random.random() * 100
# print(result)


# result = int(random.uniform(10,100))
# print(result)

# result = random.randint(1,100)
# print(result)


# names = ['ali','yağmur','deniz','cenk']
# result = names[random.randint(0,len(names) - 1)]
# print(result)


# names = ['ali','yağmur','deniz','cenk']
# result = random.choice(names)
# print(result)


# greeting = 'hello there'
# result = random.choice(greeting)
# print(result)

# liste = list(range(10))
# random.shuffle(liste)
# print(liste)

# liste = list(range(100))
# result = random.sample(liste,3)
# print(result)

names = ['ali','yağmur','deniz','cenk']
result = random.sample(names,3)
print(result)

