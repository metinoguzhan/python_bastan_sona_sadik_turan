import numpy as np

'''
numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)

# print(numbers1)                 # output [50 40 55 20 79 29]
# print(numbers2)                 # output [46 74 57 20 44 51]

result = numbers1 + numbers2    # output [ 96 114 112  40 123  80]
result = numbers1 + 10          # output [60 50 65 30 89 39]
result = numbers1 - numbers2    
result = numbers1 - 10    
result = numbers1 * numbers2    
result = numbers1 * 10    
result = numbers1 / numbers2    
result = numbers1 / 10    
result = np.sin(numbers1)
result = np.cos(numbers1)
result = np.sqrt(numbers1)
result = np.log(numbers1)
# print(result)

'''


'''

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)


multi_numbers_1 = numbers1.reshape(2,3)
multi_numbers_2 = numbers2.reshape(2,3)

print(multi_numbers_1)
print(multi_numbers_2)

result = np.vstack((multi_numbers_1,multi_numbers_2))
print(result)

result = np.hstack((multi_numbers_1,multi_numbers_2))
print(result)

'''

'''

numbers1 = np.random.randint(10,100,6)
print(numbers1)
result = numbers1 >=15
print(result)

'''

'''
numbers1 = np.random.randint(10,100,6)
print(numbers1)
result = numbers1 % 2 == 0
print(result)
'''

'''

numbers1 = np.random.randint(10,100,6)
print(numbers1)
result = numbers1 % 2 == 0
print(numbers1[result])

'''

