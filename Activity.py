import matplotlib.pyplot as plt
import numpy as np
import mplhep
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
    #Generate data and plot here


#Make some legends and axis labels here

    
