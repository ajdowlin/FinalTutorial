import matplotlib.pyplot as plt
import numpy as np
import mplhep
from matplotlib import colors

style = 'grayscale'

x = np.random.normal(size = 10000)
y = np.random.normal(size = 10000)

fig, ax = plt.subplots()

ax.set_ylabel("y axis name", loc = 'center', size = 10)
ax.set_xlabel("x axis name", loc = 'center', size = 10)
ax.set_title("Different styles don't often affect 3d plots", loc = 'center', size = 15)
hh = ax.hist2d(x, y, bins=40, norm=colors.LogNorm())
fig.colorbar(hh[3], ax=ax)

if style == 'LHCb2':
    mplhep.style.use(style)

else:
    plt.style.use(style)
    
fig.set_size_inches(10,7)
plt.show()

fig, ax = plt.subplots()

ax.set_ylabel("y axis name", loc = 'center', size = 10)
ax.set_xlabel("x axis name", loc = 'center', size = 10)
ax.set_title("But they are useful for 2D plots: this style is " + style, loc = 'center', size = 15)

plt.hist(x, bins = 20, color = 'blue')

if style == 'LHCb2':
    mplhep.style.use(style)

else:
    plt.style.use(style)
fig.set_size_inches(10,7)
plt.show()


