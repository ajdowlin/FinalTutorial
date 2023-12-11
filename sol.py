import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
nbins = 50


colors = ['red', 'blue', 'green', 'orange', 'purple']
sigmas = [1, 2, 3, 4, 5]
sizes = [1000, 1500, 2000, 2500, 3000]
mu = [0, 10, 20, 30, 40]

def Gaussian(x, norm, sigma, mu):
    u = x-mu
    return norm*np.exp(-0.5*(u**2/sigma**2))

for c, s, size, m in zip(colors, sigmas, sizes, mu):
    ys = np.random.normal(loc=m, scale=s, size=size)
    hist, bins = np.histogram(ys, bins=nbins)
    maxHeight = np.max(hist)
    
    xs = (bins[:-1] + bins[1:])/2

    start = m-4*s
    stop = m+4*s
    
    x = np.linspace(start, stop, num = 100)
    y = Gaussian(x, maxHeight, s, m)
    ax.bar(xs, hist, zs=m, zdir='y', color=c, ec=c, alpha=0.4)
    ax.plot(x, y, zs = m, zdir = 'y', color = c)

ax.legend(['data 1', 'data 2', 'data 3', 'data 4', 'data 5'])
ax.set_xlabel('X Axis (I am small)', size = 5)
ax.set_ylabel('Y Axis (I am green)', size = 10, color = 'green')
ax.set_zlabel('Z Axis (I am Comic Sans MS)', size = 10, fontname = 'Comic Sans MS')

plt.show()
