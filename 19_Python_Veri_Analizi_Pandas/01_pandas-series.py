import pandas as pd
import numpy as np


# data
numbers = [20, 30, 40, 50]
letters = ['a', 'b', 'c', 'd', 20]
scalar = 5
dictionary = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
random_numbers = np.random.randint(10,100,6)
np_arrays = np.array([20, 30, 40, 50])

# pandas_series = pd.Series()
'''
    OUTPUT: number =>   Series([], dtype: float64)
'''

# pandas_series = pd.Series(numbers)
'''
    OUTPUT: number =>   0    20
                        1    30
                        2    40
                        3    50
                        dtype: int64
'''

# pandas_series = pd.Series(letters)
'''
    OUTPUT: letters =>   0     a
                         1     b
                         2     c
                         3     d
                         4    20
                         dtype: object
'''


# pandas_series = pd.Series(scalar)
'''
    OUTPUT: scalar  =>   0    5
                         dtype: int64
'''

# pandas_series = pd.Series(scalar, index=[0, 1, 2, 3])
# pandas_series = pd.Series(scalar, [0, 1, 2, 3])
'''
    OUTPUT: scalar  =>   0    5
                         1    5
                         2    5
                         3    5
                         dtype: int64
'''

# pandas_series = pd.Series(numbers,['a','b','c','d'])
'''
    OUTPUT: numbers  =>   a    20
                          b    30
                          c    40
                          d    50
                          dtype: int64
'''

# pandas_series = pd.Series(dictionary)
'''
    OUTPUT: dictionary  =>  a    10
                            b    20
                            c    30
                            d    40
                            dtype: int64
'''

# pandas_series = pd.Series(random_numbers)
'''
    OUTPUT: random_numbers  =>  0    40
                                1    54
                                2    50
                                3    81
                                4    37
                                5    50
                                dtype: int32
'''

# pandas_series = pd.Series(np_arrays)
'''
    OUTPUT: np_arrays=>  0    20
                         1    30
                         2    40
                         3    50
                         dtype: int32
'''


pandas_series = pd.Series([20, 30, 40, 50],['a','b','c','d'])
result = pandas_series[0]
'''
    OUTPUT: result => 20
'''

result = pandas_series[-1]
'''
    OUTPUT: result => 50
'''

result = pandas_series[:2]
'''
    OUTPUT: result =>   a    20
                        b    30
'''

result = pandas_series[-2:]
'''
    OUTPUT: result =>   c    40
                        d    50
'''

result = pandas_series['a']
'''
    OUTPUT: result =>  20
'''

result = pandas_series['d']
'''
    OUTPUT: result =>  50
'''

result = pandas_series[['a','c']]
'''
    OUTPUT: result =>  a    20
                       c    40
'''

result = pandas_series[['a','c','z']]
'''
    OUTPUT: result =>  a    20.0
                       c    40.0
                       z     NaN
                       dtype: float64
'''

result = pandas_series.ndim
'''
    OUTPUT: result => 1
'''

result = pandas_series.dtype
'''
    OUTPUT: result => int64
'''

result = pandas_series.shape
'''
    OUTPUT: result => (4,)
'''

result = pandas_series.sum()
'''
    OUTPUT: result => 140
'''

result = pandas_series.max()
'''
    OUTPUT: result => 50
'''

result = pandas_series.min()
'''
    OUTPUT: result => 20
'''

result = pandas_series + pandas_series
'''
    OUTPUT: result =>   a     40
                        b     60
                        c     80
                        d    100
'''

result = pandas_series + 50
'''
    OUTPUT: result =>   a     70
                        b     80
                        c     90
                        d    100
                        dtype: int64
'''

result = np.sqrt(pandas_series)
'''
    OUTPUT: result =>   a    4.472136
                        b    5.477226
                        c    6.324555
                        d    7.071068
                        dtype: float64
'''

result = pandas_series >= 50
'''
    OUTPUT: result =>   a    False
                        b    False
                        c    False
                        d     True
                        dtype: bool
'''

result = pandas_series[pandas_series >= 40]
'''
    OUTPUT: result =>   c    40
                        d    50
                        dtype: int64
'''

result = pandas_series[pandas_series % 2 == 0]
'''
    OUTPUT: result =>   a    20
                        b    30
                        c    40
                        d    50
                        dtype: int64
'''


print(pandas_series)
print(result)
