import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
num_samples = 1000
num_bins = 20
num_frames = 400

# Generate random data
data = np.random.randn(num_samples)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(0, num_samples // num_bins)

# Create the initial histogram
hist, bins, _ = ax.hist([], bins=num_bins, range=(-5, 5), alpha=0.7)

# Update function for animation
def update(frame):
    ax.clear()

    # Update the data for the histogram
    current_data = data[: (frame + 1) * num_samples // num_frames]
    ax.hist(current_data, bins=num_bins, range=(-5, 5), alpha=0.7)

    ax.set_xlim(-5, 5)
    ax.set_ylim(0, 300)

    ax.set_title(f'Frame {frame + 1}/{num_frames}')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')

# Create the animation
animation = FuncAnimation(fig, update, frames=num_frames, interval=50)

plt.show()
