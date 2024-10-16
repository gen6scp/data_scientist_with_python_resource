import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Import this to enable 3D plotting
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

# Create a figure and a 3D axis
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.cos(R)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
#ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
#fig.colorbar(surf, shrink=0.5, aspect=5)

# Save the plot as a PNG file
plt.savefig("plots/3D_surface_plot.png")
