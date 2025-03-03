import numpy as np
import matplotlib.pyplot as plt

# arr = np.array([2, 5, 7, 8, 10, 12, 15, 18, 20, 22, 25, 30])

# plt.figure(figsize=(8, 4))  # Set figure size
# plt.boxplot(arr, vert=False)  # Horizontal box plot
# plt.grid(True)  # Add grid for better visibility
# plt.show()

# Generates grouped data
data_group1 = [np.random.normal(0, 1, 100), np.random.normal(1, 2, 100), np.random.normal(2, 1.5, 100)]
data_group2 = [np.random.normal(0, 1, 100), np.random.normal(1, 2, 100), np.random.normal(2, 1.5, 100)]
# Combines two data groups into a dataset
data = data_group1 + data_group2
print(data)
# Creates grouped boxplots

plt.boxplot(
    data, 
    positions=[1, 2, 3, 5, 6, 7], 
    tick_labels=['G1-D1', 'G1-D2', 'G1-D3', 'G2-D1', 'G2-D2', 'G2-D3'],
    boxprops=dict(color='blue'), 
    whiskerprops=dict(color='red'), 
    capprops=dict(color='green'), 
    medianprops=dict(color='orange'), 
    flierprops=dict(markerfacecolor='red', marker="o")
)

plt.title('Grouped Boxplots')
plt.xlabel('Group-Dataset')
plt.ylabel('Value')
plt.show()

