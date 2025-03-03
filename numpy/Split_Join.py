
import numpy as np
# joining of array
# Creating two 1D NumPy arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Concatenating two 1D arrays
join_arr = np.concatenate([arr1, arr2])
print(join_arr)

# Creating 2D arrays
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6],[7, 8], [9, 10]])

# Concatenating along axis 0 (rows)
np.concatenate((a, b), axis=0)

# Concatenating along axis 1 (columns), transposing b to match dimensions
print(np.concatenate((a, b.T), axis=1))

# Flattening and concatenating all elements into a 1D array
print(np.concatenate((a, b), axis=None))  # Output: array([1, 2, 3, 4, 5, 6])

# Note: This function will not preserve masking of MaskedArray inputs.

# Creating a masked array
a = np.ma.arange(3)
a[1:] = np.ma.masked  # Masking elements from index 1 onwards
print(a)  # Output: masked_array(data=[0, --, --], mask=[False, True, True])


a1 = np.array([[1, 2,5],[4, 3,5],])
a2 = np.array([[4, 5,5],[5, 6,5],])
a3 = np.array([[7, 3,5],[7, 6,5],])

# new = np.stack((a1, a2,a3), axis=1)
print(np.stack((a1, a2,a3), axis=0))#joins multiple arrays along a new dimension
print()
print(np.hstack((a1, a2,a3))) #how many rows create that depend on the how may rows present in the original array
print()
print(np.vstack((a1, a2,a3)))


#split
import numpy as np

# Step 1: Create an array
arr = np.array([1, 2, 3, 4, 5, 6])
print("Original Array:")
print(arr)

# Step 2: Split into 3 equal parts
split_arr = np.split(arr, 3)
print("\nArray Split into 3 Equal Parts:")
for part in split_arr:
    print(part)

# Step 3: Split at specific indices
split_arr = np.split(arr, [2, 4])
print("\nArray Split at Indices 2 and 4:")
for part in split_arr:
    print(part)

# Step 4: Handle error when splitting into unequal parts
try:
    split_arr = np.split(arr, 4)
except ValueError as e:
    print("\nError:", e)

# Step 5: Split at custom indices
split_arr = np.split(arr, [1, 3, 5])
print("\nArray Split at Custom Indices [1, 3, 5]:")
for part in split_arr:
    print(part)
