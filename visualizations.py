# Write code that creates two linecharts from bestTrajectory.txt and searchTrajectory.txt. Each file contains rows with two columns, separated by space. The first is the row number and should be the x axis. The second is the value of the y axis. Both lines should be on the same axis with different colors.

# Solution
import matplotlib.pyplot as plt
import numpy as np

# Read the data from the files
best_trajectory = np.loadtxt('bestTrajectory.txt')
search_trajectory = np.loadtxt('searchTrajectory.txt')

# Create a figure and two subplots vertically aligned
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

# Create the line charts
ax1.plot(best_trajectory[:, 0], best_trajectory[:, 1], label='Best Trajectory')
ax2.plot(search_trajectory[:, 0], search_trajectory[:, 1], label='Search Trajectory')

# Add labels and title to the first subplot
ax1.set_ylabel('Value')
ax1.set_title('Best Trajectory')
ax1.legend()

# Add labels and title to the second subplot
ax2.set_xlabel('Row Number')
ax2.set_ylabel('Value')
ax2.set_title('Search Trajectory')
ax2.legend()

# Show the plot
plt.show()

