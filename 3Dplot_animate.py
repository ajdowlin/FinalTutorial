import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Frequency')

bins = 30
xedges = np.linspace(-4, 4, bins + 1)
yedges = np.linspace(-4, 4, bins + 1)

hist, _, _ = np.histogram2d([], [], bins=[xedges, yedges])

xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0
dx = dy = 0.5
bars = [ax.bar3d(xpos, ypos, zpos, dx, dy, np.zeros_like(zpos), shade=True)]

num = 10000
data = np.random.normal(size=(num, 2))

n = num

def update(curr):
    if curr == n:
        a.event_source.stop()

    plt.cla()

    # Update the 3D histogram data
    current_data = data[:curr*4, :2]
    hist, _, _ = np.histogram2d(current_data[:, 0], current_data[:, 1], bins=[xedges, yedges])

    # Update the heights of the bars in the 3D histogram
    #for bar in bars:
    #    bar.remove()
    bars[0] = ax.bar3d(xpos, ypos, zpos, dx, dy, hist.ravel(), shade=True, color = 'red')

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Frequency')

    ax.set_title('Animated 3D Histogram Stack-Up')
    ax.annotate('n={}'.format(curr), [3, 3])

# Set up the histogram animation
a = animation.FuncAnimation(fig, update, frames=n, interval=1)

plt.show()
