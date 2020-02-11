import numpy as np


numbers = np.array([0,5,10,15,20,25,50,75])
result = numbers[5]      # output 25
result = numbers[-1]     # output 75
result = numbers[0:3]    # output [ 0  5 10]
result = numbers[:3]     # output [ 0  5 10]
result = numbers[3:]     # output [15 20 25 50 75]
result = numbers[::]     # output [ 0  5 10 15 20 25 50 75]
result = numbers[::-1]   # output [75 50 25 20 15 10  5  0]
result = numbers[::-2]   # output [75 25 15  5]

# print(result)

numbers = np.array([[0,5,10],[15,20,25],[50,75,85]])
result = numbers[0]             # output [ 0  5 10]
result = numbers[2]             # output [50 75 85]
result = numbers[0,2]           # output 10
result = numbers[2,1]           # output 75
result = numbers[:,2]           # output [10 25 85]
result = numbers[:,0]           # output [ 0 15 50]
result = numbers[:,0:2]         # output [[ 0  5] [15 20][50 75]]
result = numbers[-1:,0:2]       # output [[50 75]]
result = numbers[-1,:]          # output [50 75 85]
result = numbers[:2,:2]         # output [[ 0  5] [15 20]]

# print(result)            


arr1 = np.arange(0,10)
# arr2 = arr1         # referans kopyalama
arr2 = arr1.copy()
print(arr1)
print(arr2)

arr2[0] = 20
print(arr1)
print(arr2)
