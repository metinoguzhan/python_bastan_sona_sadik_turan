# def my_decorator(func):
#     def wrapper(name):
#         print("foksiyondan önceki işlemler")
#         func(name)
#         print('fonksiyondan sonraki işlemler')
#     return wrapper

# @my_decorator
# def sayHello(name):
#     print('hello ', name)

# def sayGreeting(name):
#     print('greeting', name)


# sayHello("Metin")


# hello = my_decorator(sayHello)
# hello()

# greeting = my_decorator(sayGreeting)
# greeting()


import math
import time

def calculate_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish = time.time()
        print('fonksiyonnn ' + func.__name__ +" "+ str(finish-start) + ' saniye sürdü.')
    return inner

@calculate_time
def usalma(a, b):
    print(math.pow(a, b))
   
@calculate_time
def faktoriyel(num):
    print(math.factorial(num))

@calculate_time
def toplama(a,b):
    print(a+b)


usalma(2,3)
faktoriyel(5)
toplama(5,9)
