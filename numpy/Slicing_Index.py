import numpy as np

# Indexing in a 3D Array
print("=== Indexing in a 3D Array ===")
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("3D Array:")
print(arr)
print("Element at index [0, 1, 2]:", arr[0, 1, 2])  # Output: 6

# Slicing in a 2D Array
print("\n=== Slicing in a 2D Array ===")
arr_2D = np.array([[12, 23, 34, 45], [45, 56, 78, 99]])
print("2D Array:")
print(arr_2D)

row_start = 1
row_stop = 2
row_jump = 1
col_start = 0
col_stop = len(arr_2D[1])  # Length of the second row (4)
col_jump = 2

print("Sliced 2D Array:")
print(arr_2D[row_start:row_stop:row_jump, col_start:col_stop:col_jump])  # Output: [[45 78]]

# Additional Examples of Indexing and Slicing
print("\n=== Additional Examples of Indexing and Slicing ===")

# Example 1: Indexing in a 2D Array
print("\nExample 1: Indexing in a 2D Array")
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array:")
print(arr)
print("Element at row 1, column 2:", arr[1, 2])  # Output: 6
print("Entire second row:", arr[1, :])  # Output: [4 5 6]
print("Entire third column:", arr[:, 2])  # Output: [3 6 9]

# Example 2: Slicing in a 3D Array
print("\nExample 2: Slicing in a 3D Array")
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("3D Array:")
print(arr)
print("First 2D array:")
print(arr[0, :, :])  # Output: [[1 2 3], [4 5 6]]
print("Second row of both 2D arrays:")
print(arr[:, 1, :])  # Output: [[4 5 6], [10 11 12]]
print("First column of all 2D arrays:")
print(arr[:, :, 0])  # Output: [[1 4], [7 10]]

# Example 3: Slicing with Steps
print("\nExample 3: Slicing with Steps")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("1D Array:")
print(arr)
print("Slice with a step of 2:", arr[::2])  # Output: [1 3 5 7 9]
print("Slice from index 1 to 7 with a step of 3:", arr[1:7:3])  # Output: [2 5]

# Example 4: Negative Indexing and Slicing
print("\nExample 4: Negative Indexing and Slicing")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("1D Array:")
print(arr)
print("Last element:", arr[-1])  # Output: 9
print("Last three elements:", arr[-3:])  # Output: [7 8 9]
print("Reversed array:", arr[::-1])  # Output: [9 8 7 6 5 4 3 2 1]