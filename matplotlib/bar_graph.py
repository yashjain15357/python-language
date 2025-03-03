# Importing necessary libraries
import matplotlib.pyplot as plt  # Matplotlib for plotting graphs
import numpy as np  # Numpy for handling arrays and numerical operations

# List of programming languages
language = ["python", "java", "c++", "c", "javascript"]

# Creating an array for the x-axis positions
X_axis = np.arange(len(language))  # Generates array indices [0,1,2,3,4] for bar positions

# Number of users for each programming language
user = [45, 78, 63, 49, 23]  # Data for first user group
user1 = [36, 29, 56, 32, 20]  # Data for second user group

# Plotting bar chart for 'user' group
plt.bar(X_axis - 0.2, user, width=0.4, label="user", color="r",align="edge",alpha=0.8,hatch='/')  
# X_axis - 0.2 shifts bars left to avoid overlap
# width=0.4 controls the width of each bar
# color="r" sets the color of bars to red
# label="user" assigns a label to this group
# align:	Positioning of bars ('center' or 'edge')
# edgecolor:	Color of the bar edges
# linewidth:	Thickness of the bar edges
# alpha:	Transparency level (0 to 1)
# hatch:	Pattern inside the bars (e.g., /, \, x, o)
# bottom:	Shifts bars vertically (useful for stacking)

# Plotting bar chart for 'user1' group
plt.bar(X_axis + 0.2, user1, width=0.4, label="user1", color="g",hatch='-',align="edge")   
# X_axis + 0.2 shifts bars right to separate from the first set of bars
# color="g" sets the color of bars to green
# label="user1" assigns a label to this group

# Setting the x-axis labels as programming languages
plt.xticks(X_axis, language)  
# Aligns x-axis positions with the names of the languages

# Setting the title of the graph
plt.title("Programming Language")  
# Sets the title of the bar chart

# Label for x-axis
plt.xlabel("Language")  
# Describes what the x-axis represents

# Label for y-axis
plt.ylabel("No of Users")  
# Describes what the y-axis represents

# Display legend for the two groups
plt.legend()  
# Displays the legend showing 'user' in red and 'user1' in green

# Display the graph
plt.show()  
# Renders the bar chart on the screen
