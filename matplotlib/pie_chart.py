import numpy as np  # Importing NumPy for numerical operations
import matplotlib.pyplot as plt  # Importing Matplotlib for data visualization

# Pie charts are useful for visualizing the proportional distribution of data.
# The pie() function in Matplotlib helps create a pie chart.

# ------ Step 1: Define the Data ------
# Data represents the values for different programming languages.
data = np.array([23, 17, 35, 29, 12, 40])  # List of numerical values

# Labels represent the categories corresponding to the data.
pro_language = ["C", "C++", "Python", "Java", "JavaScript", "PHP"]

# Colors for each slice of the pie chart.
colors = ("orange", "cyan", "brown", "grey", "indigo", "beige")

# Explode values to separate slices (values between 0 and 1, where 0 means no separation).
explode = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]  # Increasing separation for each slice

# ------ Step 2: Create a Simple Pie Chart ------
plt.pie(data, labels=pro_language, colors=colors)  # Creating a basic pie chart

# ------ Step 3: Create a More Customized Pie Chart ------
# `plt.subplots()` creates a new figure and axis (optional, used for better structure).
plt.subplots()

# Creating a pie chart with more customization.
plt.pie(
    data, 
    labels=pro_language, 
    explode=explode,  # Separates the slices
    colors=colors, 
    wedgeprops={'linewidth': 2, "edgecolor": "green"},  # Green borders around slices
    textprops=dict(color="magenta"),  # Text labels appear in magenta color
    shadow=True,  # Adds a shadow effect to the pie chart
    autopct='%1.1f%%'
)

# ------ Step 4: Add a Legend ------
plt.legend()  # Displays a legend to identify categories

# ------ Step 5: Display the Chart ------
plt.show()  # Shows the pie charts

# ------ Alternative Example ------
# A smaller dataset with a simpler pie chart representation.
sizes = [40, 30, 20, 10]  # Data values
labels = ['A', 'B', 'C', 'D']  # Category labels
explode = (0, 0.1, 0, 0.2)  # Only slices 'B' and 'D' will be exploded (highlighted)

# Creating a figure and axis for better structuring.
fig, ax = plt.subplots()

# Creating a pie chart with percentages displayed on slices.
ax.pie(sizes, labels=labels, autopct='%1.1f%%')  # autopct adds percentage labels

# Show the final plot
plt.show()

# This tutorial provides a beginner-friendly guide to creating pie charts using Matplotlib.
# Experiment with colors, explode values, and other properties to customize your charts!
