#!/usr/bin/env python3

import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from shapely.ops import unary_union

def plot_polygon(ax, polygon, color='blue', linewidth=1, fill=False, fill_color='blue', alpha=0.5):
    x, y = polygon.exterior.xy
    ax.plot(x, y, color=color, linewidth=linewidth)
    if fill:
        ax.fill(x, y, alpha=alpha, color=fill_color)

# Define two polygons
polygon1 = Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])
polygon2 = Polygon([(1, 1), (3, 1), (3, 3), (1, 3)])

# Compute the union of the two polygons
union_polygon = unary_union([polygon1, polygon2])

# Print the coordinates of the union polygon
print("Union of polygon1 and polygon2:", list(union_polygon.exterior.coords))

# Plotting
fig, ax = plt.subplots()

# Plot the original polygons
plot_polygon(ax, polygon1, color='red', fill=True, fill_color='red', alpha=0.3)
plot_polygon(ax, polygon2, color='green', fill=True, fill_color='green', alpha=0.3)

# Plot the union polygon
plot_polygon(ax, union_polygon, color='blue', linewidth=2, fill=True, fill_color='blue', alpha=0.3)

# Setting plot limits
minx, miny, maxx, maxy = union_polygon.bounds
ax.set_xlim(minx - 1, maxx + 1)
ax.set_ylim(miny - 1, maxy + 1)

# Show plot
plt.show()

