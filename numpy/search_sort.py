import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8,3,6,8,34,8,348,2])

x = np.where(arr%2 == 0) #return the index according to the searching condition

print(x)

import numpy as np

arr = np.array([6, 7, 8, 9])

temp = np.searchsorted(arr, 7, side='right') #Find the indexes where the value 7 should be inserted, starting from the right:
temp1 = np.searchsorted(arr, 7, side='left') #Find the indexes where the value 7 should be inserted, starting from the left:
temp2 = np.searchsorted(arr, [2, 4, 6])#Find the indexes where the values 2, 4, and 6 should be inserted:

print(temp)