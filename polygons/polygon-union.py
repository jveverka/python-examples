#!/usr/bin/env python3
from shapely.geometry import Polygon
from shapely.ops import unary_union

# Define two polygons
polygon1 = Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])
polygon2 = Polygon([(1, 1), (3, 1), (3, 3), (1, 3)])

# Compute the union of the two polygons
union_polygon = unary_union([polygon1, polygon2])

# Print the coordinates of the union polygon
print("Union of polygon1 and polygon2:", list(union_polygon.exterior.coords))
