"""
Rendering module, responsible for *fast* png creation.
"""

import StringIO
import colormaps

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

COLORMAPS = {
    'temperature': colormaps.temperature,
    'mslp': colormaps.mslp,
    'elevation': colormaps.elevation
    }

def draw_tile(grid, cmap, vmin, vmax, dpi=75, alpha=0.75):
    """ Draws a tile """

    fig = Figure(dpi=dpi, edgecolor='none')
    fig.patch.set_alpha(0.0)

    # Form the graphic
    ax = fig.add_axes((0,0,1,1))
    ax.matshow(grid, interpolation='nearest', alpha=alpha, vmin=vmin, vmax=vmax, cmap=COLORMAPS[cmap])
    ax.axis('off')
    ax.axis('tight')

    # Write the PNG file to a string.
    canvas = FigureCanvas(fig)
    png_output = StringIO.StringIO()
    canvas.print_png(png_output, transparent=True)
    
    return png_output.getvalue()