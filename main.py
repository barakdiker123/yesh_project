#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# Set the random seed for reproducibility
# np.random.seed(42)

# Generate random samples from the normal distributions
mean1 = 7
variance1 = 16
mean2 = 7
variance2 = 14
sample_size = 10000
data1 = np.random.normal(mean1, np.sqrt(variance1), sample_size)
data2 = np.random.normal(mean2, np.sqrt(variance2), sample_size)

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(10, 4), sharey=True)

# Plotting the histograms
axs[0].hist(data1, bins=10, density=True, alpha=0.7, color='red', label='Std Dev 4')
axs[1].hist(data2, bins=10, density=True, alpha=0.7, color='blue', label='Std Dev 3.74')

# Plotting the normal distribution curves
x = np.linspace(min(min(data1), min(data2)), max(max(data1), max(data2)), 100)
y1 = 1 / (np.sqrt(2 * np.pi * variance1)) * np.exp(-0.5 * ((x - mean1) / np.sqrt(variance1))**2)
y2 = 1 / (np.sqrt(2 * np.pi * variance2)) * np.exp(-0.5 * ((x - mean2) / np.sqrt(variance2))**2)
axs[0].plot(x, y1, color='black')
axs[1].plot(x, y2, color='black')

# Set the same x-axis range for both subplots
min_x = min(min(data1), min(data2))
max_x = max(max(data1), max(data2))
axs[0].set_xlim(min_x, max_x)
axs[1].set_xlim(min_x, max_x)

# Add labels and titles to subplots
axs[0].set_xlabel('Value')
axs[0].set_ylabel('Probability Density')
axs[0].set_title('Std Dev 4')
axs[1].set_xlabel('Value')
axs[1].set_ylabel('Probability Density')
axs[1].set_title('Std Dev 3.74')

# Add a common title to the figure
fig.suptitle('Same annual return, 7%\nDifferent distributions')

# Add a legend to the first subplot
axs[0].legend()

# Adjust spacing between subplots
plt.tight_layout()

# Show the plot
plt.show()
