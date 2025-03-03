import numpy as np

# Generate a simple 2D array using numpy
simple_array = np.array([[12, 12, 12, 12, 12], [23, 45, 23, 23, 7]])
print("Simple 2D Array:")
print(simple_array)

# Generate a 1D random array using rand() function
# This generates random numbers between 0 and 1
rand_1D_arr = np.random.rand(5)
print("\nRandom 1D Array (values between 0 and 1):")
print(rand_1D_arr)

# Generate a 2D random array using rand() function
rand_2D_arr = np.random.rand(5, 3)  # 5 rows and 3 columns
print("\nRandom 2D Array (values between 0 and 1):")
print(rand_2D_arr)

# Generate a 1D random array using randn() function
# This generates random numbers from a standard normal distribution (-1 to 1, mean=0)
randn_1D_arr = np.random.randn(5)
print("\nRandom 1D Array (standard normal distribution):")
print(randn_1D_arr)

# Generate a 2D random array using randn() function
randn_2D_arr = np.random.randn(5, 3)  # 5 rows and 3 columns
print("\nRandom 2D Array (standard normal distribution):")
print(randn_2D_arr)

# Generate a 1D random array using ranf() function
# This generates random numbers between 0 and 1 (similar to rand but explicitly)
ranf_1D_arr = np.random.ranf(5)
print("\nRandom 1D Array (values between 0 and 1 using ranf):")
print(ranf_1D_arr)

# Generate a 1D random integer array using randint() function
# This generates random integers between the specified min and max values
min_val = 5
max_val = 10
num_elements = 7  # Total number of elements in the array
randint_1D_arr = np.random.randint(min_val, max_val, num_elements)
print("\nRandom 1D Integer Array (values between 5 and 10):")
print(randint_1D_arr)

# Attempt to generate a 2D random integer array using randint()
# Note: np.random.randint does not support non-positive shapes
# This will throw an error if you try it. Correct usage would be with positive dimensions.
try:
    randint_2D_arr = np.random.randint(5, 3, (2, 3))  # Example corrected to 2 rows and 3 columns
    print("\nRandom 2D Integer Array:")
    print(randint_2D_arr)
except ValueError as e:
    print("\nError generating 2D Integer Array:", e)

