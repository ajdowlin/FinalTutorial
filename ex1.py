import matplotlib.pyplot as plt
import numpy as np


def exponent(x, A, c):
    return A*np.exp(c*x)

x = np.linspace(start = 0, stop = 20, num = 500)
y1 = exponent(x, 1, 1)
y2 = exponent(x, 2, 0.5)
y3 = exponent(x, 3, 0.1)

fig, ax = plt.subplots()

# simple way of plotting. Hard to interpret data though

ax.plot(x, y1)
ax.plot(x, y2)
ax.plot(x, y3)

plt.show()


#lets try that again

fig, ax = plt.subplots()

ax.plot(x, y1, color = 'blue', linestyle = 'none', marker = 'o', markersize = '5')
ax.plot(x, y2, color = 'red', linestyle = 'dashed', linewidth = '3')
ax.plot(x, y3, color = 'green', linestyle = 'dashdot', linewidth = '5')

plt.yscale("log")
ax.legend(['data 1', 'data 2', 'data 3'], loc = 'upper left')


plt.show()

        
