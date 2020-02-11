def square(num): return num **2

numbers = [1,3,5,9,10,4,8]

result = list(map(square,numbers))
print(result)



for item in map(square,numbers):
    print(item)



sayilar = map(lambda num: num ** 3,numbers)
print(list(sayilar))


## 

square2 = lambda num: num ** 4
sayilar = map(square2,numbers)
print(list(sayilar))

print(square2(9))

## filter
def check_even(num):
    return num % 2 == 0

result = list(filter(check_even,map(lambda v: v ** 2,numbers)))
print(result)


result = list(filter(check_even,numbers))
print(result)

result = list(filter(lambda val: val % 2 == 0,numbers))
print(result)
print(result[1])