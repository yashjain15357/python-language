import numpy as np

# ============================================
# 1. Understanding the `shape` attribute
# ============================================

# Create a 1D array
arr_1d = np.array([1, 2, 3, 4, 5, 6])
print("1D Array:")
print(arr_1d)
print("Shape of 1D array:", arr_1d.shape)  # Output: (6,)

# Create a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:")
print(arr_2d)
print("Shape of 2D array:", arr_2d.shape)  # Output: (2, 3)

# Create a 3D array
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n3D Array:")
print(arr_3d)
print("Shape of 3D array:", arr_3d.shape)  # Output: (2, 2, 2)

# ============================================
# 2. Using the `reshape` function
# ============================================

# Reshape a 1D array into a 2D array
reshaped_2d = arr_1d.reshape(2, 3)  # Reshape into 2 rows and 3 columns
print("\nReshaped 1D to 2D Array:")
print(reshaped_2d)
print("Shape of reshaped 2D array:", reshaped_2d.shape)  # Output: (2, 3)

# Reshape a 1D array into a 3D array
reshaped_3d = arr_1d.reshape(2, 3, 1)  # Reshape into 2 blocks, 3 rows, and 1 column
print("\nReshaped 1D to 3D Array:")
print(reshaped_3d)
print("Shape of reshaped 3D array:", reshaped_3d.shape)  # Output: (2, 3, 1)

# Reshape a 2D array into another 2D array
reshaped_2d_2 = arr_2d.reshape(3, 2)  # Reshape into 3 rows and 2 columns
print("\nReshaped 2D to 2D Array:")
print(reshaped_2d_2)
print("Shape of reshaped 2D array:", reshaped_2d_2.shape)  # Output: (3, 2)

# Reshape a 2D array into a 1D array
reshaped_1d = arr_2d.reshape(-1)  # Flatten the array into 1D
print("\nReshaped 2D to 1D Array:")
print(reshaped_1d)
print("Shape of reshaped 1D array:", reshaped_1d.shape)  # Output: (6,)

# ============================================
# 3. Important Notes on Reshaping
# ============================================

# Reshaping must maintain the total number of elements
try:
    invalid_reshape = arr_1d.reshape(3, 4)  # This will raise an error
except ValueError as e:
    print("\nError during reshaping:", e)

# Using -1 in reshape to automatically calculate dimensions
auto_reshape = arr_1d.reshape(2, -1)  # Automatically calculate columns
print("\nAuto Reshape (2 rows, auto columns):")
print(auto_reshape)
print("Shape of auto reshaped array:", auto_reshape.shape)  # Output: (2, 3)

# ============================================
# 4. Practical Example: Reshaping for Matrix Operations
# ============================================

# Create a 1D array of 12 elements
arr = np.arange(1, 13)  # [1, 2, 3, ..., 12]
print("\nOriginal 1D Array:")
print(arr)

# Reshape into a 3x4 matrix
matrix = arr.reshape(3, 4)
print("\nReshaped 3x4 Matrix:")
print(matrix)

# Transpose the matrix
transposed_matrix = matrix.T
print("\nTransposed Matrix (4x3):")
print(transposed_matrix)