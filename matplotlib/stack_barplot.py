# Import necessary libraries
import numpy as np 
import matplotlib.pyplot as plt 

# Define the width of each bar in the grouped bar chart
barWidth = 0.25  

# Define data for students passed in IT, ECE, and CSE branches over different years
IT = [12, 30, 1, 8, 22]   # IT students passed
ECE = [28, 6, 16, 5, 10]   # ECE students passed
CSE = [29, 3, 24, 25, 17]  # CSE students passed

# Compute the x-axis positions for each group of bars
br1 = np.arange(len(IT))  # Initial positions for IT bars (0,1,2,3,4)
br2 = [x + barWidth for x in br1]  # Shift ECE bars to the right(0.25,1.25,2.25,3.25,4.25)
br3 = [x + barWidth for x in br2]  # Shift CSE bars further to the right (0.50,1.50,2.50,3.50,4.50)

# Create the grouped bar chart
plt.bar(br1, IT, color='r', width=barWidth, edgecolor='grey', label='IT')  
plt.bar(br2, ECE, color='g', width=barWidth, edgecolor='grey', label='ECE')  
plt.bar(br3, CSE, color='b', width=barWidth, edgecolor='grey', label='CSE')  

# Label the x-axis and y-axis
plt.xlabel('Year', fontweight='bold', fontsize=15)  
plt.ylabel('Students Passed', fontweight='bold', fontsize=15)  

# Set the x-axis ticks (placing them in the center of the grouped bars)
plt.xticks([r + barWidth for r in range(len(IT))],  
           ['2015', '2016', '2017', '2018', '2019'])  

# Add a legend to differentiate the three branches
plt.legend()  

# Display the bar chart
plt.show()  
