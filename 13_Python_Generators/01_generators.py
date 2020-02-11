# def cube():
#     result = []

#     for i in range(5):
#         result.append(i**3)
#     return result

# print(cube())


def cube():
    for i in range(5):
        yield i ** 3


# generator = cube()
# iterator = iter(generator)

# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))

for i in cube():
    print(i)


# liste = [i**3 for i in range(5)]
generator = (i**3 for i in range(5))
print(next(generator))
print(next(generator))
print(next(generator))

for i in generator:
    print(i)