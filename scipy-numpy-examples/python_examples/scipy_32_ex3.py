import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# Defining a function
ripple = lambda x, y: np.sqrt(x ** 2 + y ** 2)\
		+ np.sin(x ** 2 + y ** 2)

# Generarting gridded data
grid_x, grid_y = np.mgrid[0:5:1000j, 0:5:1000j]

# Generating saplte that interpolation function will see
xy = np.random.rand(1000, 2)
saplte = ripple(xy[:, 0] * 5, xy[:, 1] * 5)

# Interpolating data
grid_z0 = griddata(xy * 5, saplte, (grid_x, grid_y), method='cubic')

# Making figure.
fig = plt.figure(figsize=(8, 4))

x0, x1 = 0, 1000
y0, y1 = 0, 1000
ax1 = fig.add_subplot(121)
ax1.imshow(ripple(grid_x, grid_y).T, cmap=plt.cm.RdYlGn,#如何去找这种属性？找不到---->已解决，在colormaps() (in module matplotlib.pyplot)里面
			interpolation='nearest')
ax1.scatter(xy[:, 0] * 1e3, xy[:, 1] * 1e3, facecolor='black',
	        edgecolor='none', s=1)
ax1.xaxis.set_visible(False)
ax1.yaxis.set_visible(False)
ax1.set_xlim(x0, x1)
ax1.set_ylim(y0, y1)

ax2 = fig.add_subplot(122)
ax2.imshow(grid_z0.T, cmap=plt.cm.Blues, interpolation='nearest',
	       vmin=0.05, vmax=7.87)
ax2.xaxis.set_visible(False)
ax2.yaxis.set_visible(False)
ax2.set_xlim(x0, x1)
ax2.set_ylim(y0, y1)

fig.savefig('scipy_32_ex3.png', bbox_inches='tight')
