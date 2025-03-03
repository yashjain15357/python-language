import numpy as np

# Create integer array and check its data type
intArr = np.array([3, 3, 5, 5])
print("Integer Array Data Type:", intArr.dtype)

# Create float array and check its data type
floatArr = np.array([3.0, 3.9, 5.5, 5.4])
print("\nFloat Array Data Type:", floatArr.dtype)

# Create string array and check its data type
stringArr = np.array(["a", "as", "as", "f"])
print("\nString Array Data Type:", stringArr.dtype)

# Create a mixed-type array (Note: Numpy converts all elements to a common type, here string)
mixedArr = np.array([3.0, 3.9, 5.5, 5.4, "sf", "df"])
print("\nMixed Array Data Type:", mixedArr.dtype)

# Note:
# - Numpy determines the data type of an array based on its elements.
# - If elements are of different types, Numpy upcasts to the most general type (e.g., integers to floats, numbers to strings).

# Change data type explicitly using 'dtype' parameter
# Integer array with dtype specified as int8 (8-bit integer)
change_data_int8 = np.array([1, 5, 7, 8, 9, 7], dtype=np.int8)
print("\nInteger Array with int8 Data Type:", change_data_int8.dtype)
print(change_data_int8)

# Float array with dtype specified using short form ('f' for float32)
change_data_float = np.array([1, 5, 7, 8, 9, 7], dtype="f")
print("\nFloat Array with float32 Data Type:", change_data_float.dtype)
print(change_data_float)

# Convert array data type using astype() method
original_array = np.array([1, 5, 7, 8, 9, 7])
# Convert integer array to string array
change_data_str = original_array.astype(str)
print("\nOriginal Integer Array:", original_array)
print("Converted String Array:", change_data_str)
print("Data Type of Original Array:", original_array.dtype)
print("Data Type of Converted Array:", change_data_str.dtype)

# Additional Examples:
# Creating boolean arrays
boolArr = np.array([True, False, True, False])
print("\nBoolean Array:", boolArr)
print("Boolean Array Data Type:", boolArr.dtype)

# Creating an array with complex numbers
complexArr = np.array([1 + 2j, 3 - 4j, 5 + 6j])
print("\nComplex Number Array:", complexArr)
print("Complex Array Data Type:", complexArr.dtype)

# Converting float array to integer using astype (note: truncates decimal part)
float_to_int = floatArr.astype(int)
print("\nConverted Float to Integer Array:", float_to_int)
print("Data Type After Conversion:", float_to_int.dtype)

# Notes:
# - astype() creates a new array with the specified data type without modifying the original array.
# - Be cautious when converting between data types as it may lead to data loss (e.g., float to int truncates decimals).

# Exploring possibilities of Numpy arrays:
# - Arrays can store various data types like int, float, string, boolean, or complex numbers.
# - Mixed data types in an array result in upcasting to the most general type.
# - Arrays can be reshaped and manipulated easily, making Numpy a powerful tool for numerical computations.
