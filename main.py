import numpy as np
import pandas as pd

letters = ['a', 'b', 'c']
numbers = [1,2,3]
np_arr = np.array(numbers)
dict = {'a':1, 'b':2, 'c':3}
print(letters)
print(numbers)
print(np_arr)
print(pd.Series(data=numbers))
print(pd.Series(data=numbers, index=letters))
print(pd.Series(numbers, letters))
print(pd.Series(data=np_arr))
print(pd.Series(np_arr))
print(pd.Series(np_arr,letters))
print(dict)
print(pd.Series(dict))
print(pd.Series(data=letters))
life_long_average = pd.Series([84.7, 84.5, 83.7], ['Hong Kong', 'Japan', 'Singapore'])
print(life_long_average)
print(life_long_average['Hong Kong'])
life_long_average1 = pd.Series([84.7, 84.5, 83.7], ['Hong Kong', 'Japan', 'Singapore'])
print(life_long_average+life_long_average1)
life_long_average2 = pd.Series([84.7, 84.5, 83.7], ['USA', 'Japan', 'Singapore'])
print(life_long_average+life_long_average2)
