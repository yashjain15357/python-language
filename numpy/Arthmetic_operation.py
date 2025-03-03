# Arithmetic Operations in Array using NumPy
import numpy as np

# Example for 1D array
arr1 = np.array([11, 2, 3, 4, 5])
arr2 = np.array([11, 2, 3, 4, 5])

# Addition
addArr1 = arr1 + arr2  # Element-wise addition
addArr2 = np.add(arr1, arr2)  # Using NumPy's add function

# Subtraction
subArr1 = arr1 - arr2  # Element-wise subtraction
subArr2 = np.subtract(arr1, arr2)  # Using NumPy's subtract function

# Multiplication
multiArr1 = arr1 * arr2  # Element-wise multiplication
multiArr2 = np.multiply(arr1, arr2)  # Using NumPy's multiply function

# Division
diviArr1 = arr1 / arr2  # Element-wise division
diviArr2 = np.divide(arr1, arr2)  # Using NumPy's divide function

# Modulus
modArr1 = arr1 % arr2  # Element-wise modulus
modArr2 = np.mod(arr1, arr2)  # Using NumPy's mod function

# Printing results for 1D arrays
print("1D Array Operations:")
print("Addition (Using '+'):", addArr1)
print("Addition (Using np.add):", addArr2)
print("Subtraction (Using '-'):", subArr1)
print("Subtraction (Using np.subtract):", subArr2)
print("Multiplication (Using '*'):", multiArr1)
print("Multiplication (Using np.multiply):", multiArr2)
print("Division (Using '/'):", diviArr1)
print("Division (Using np.divide):", diviArr2)
print("Modulus (Using '%'):", modArr1)
print("Modulus (Using np.mod):", modArr2)

# Example for 2D arrays
arr2D_1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2D_2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Arithmetic operations for 2D arrays
add2D = np.add(arr2D_1, arr2D_2)
sub2D = np.subtract(arr2D_1, arr2D_2)
multi2D = np.multiply(arr2D_1, arr2D_2)
divi2D = np.divide(arr2D_1, arr2D_2)
mod2D = np.mod(arr2D_1, arr2D_2)

# Printing results for 2D arrays
print("\n2D Array Operations:")
print("Addition:\n", add2D)
print("Subtraction:\n", sub2D)
print("Multiplication:\n", multi2D)
print("Division:\n", divi2D)
print("Modulus:\n", mod2D)

# Limitations of arithmetic operations in NumPy arrays
"""
1. Shape Mismatch: Arithmetic operations require the arrays to have the same shape or be compatible for broadcasting.
   Example: If arr1 has shape (3,) and arr2 has shape (3, 2), operations like arr1 + arr2 will raise a ValueError.
2. Division by Zero: Performing division by zero will result in `inf` or `nan` values instead of raising an exception.
3. Modulus with Zero: Using the modulus operator (%) with zero will raise a ZeroDivisionError.
4. Data Type Limitations: Operations are performed according to the array's dtype, which might lead to overflow in integer types.
5. Memory Consumption: NumPy arrays are memory-efficient but still limited by available system memory for very large arrays.
"""
