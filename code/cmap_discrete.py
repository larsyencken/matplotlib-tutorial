"""
Example of matplotlib colormaps
http://matplotlib.org/api/colors_api.html
"""

import numpy as np

import matplotlib
from matplotlib import figure
from matplotlib.backends.backend_agg import (
FigureCanvasAgg as FigureCanvas)

import matplotlib.cm as mcm
import matplotlib.colors as mcolors

data = np.random.randn(50,50)

fig = figure.Figure()

canvas = FigureCanvas(fig)


cmap = mcm.RdBu


ax1 = fig.add_subplot(1,2,1)
plt1 = ax1.imshow(data, interpolation='nearest',
				  cmap=cmap)
cbar1 = fig.colorbar(plt1, ax=ax1, fraction=0.045)

norm = mcolors.BoundaryNorm(np.arange(-2,2.5,.5), cmap.N)

ax2 = fig.add_subplot(1,2,2)
plt2 = ax2.imshow(data, interpolation='nearest', cmap='RdBu', norm=norm)
cbar2 = fig.colorbar(plt2, ax=ax2, fraction=0.045,extend='both')
cbar2.cmap.set_over('green')
cbar2.cmap.set_under('orange')
cbar2.set_label("Random Data")
fig.subplots_adjust(wspace=.4)
canvas.print_figure('figures/cmapdiscrete.png', 
		facecolor='lightgray')
