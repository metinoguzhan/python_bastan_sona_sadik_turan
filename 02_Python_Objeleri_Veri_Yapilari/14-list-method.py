numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a','g','s','b','y','a','s']

val = min(numbers)
print(val)

val = max(numbers)
print(val)


val = min(letters)
print(val)

val = max(letters)
print(val)


val = numbers[3:6]
print(val)

val = numbers[:3]
print(val)

val = numbers[4:]
print(val)


numbers[4] = 40
print(numbers)

numbers.append(59)
print(numbers)

numbers.insert(3,78)
print(numbers)

numbers.insert(-1,52)
print(numbers)

numbers.pop()
print(numbers)


numbers.pop(-1)
print(numbers)

numbers.pop(1)
print(numbers)

numbers.remove(9)
print(numbers)


numbers.sort()
print(numbers)

letters.sort()
print(letters)


letters.reverse()
print(letters)

print(len(letters))


print(letters.count('a'))

numbers.clear()
print(numbers)