#!/usr/bin/env python3

import json
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from shapely.ops import unary_union

in_file_path = 'polygons.json'
out_file_path = 'polygons-out.json'

show_plot = False

def plot_polygon(ax, polygon, color='blue', linewidth=1, fill=False, fill_color='blue', alpha=0.5):
    x, y = polygon.exterior.xy
    ax.plot(x, y, color=color, linewidth=linewidth)
    if fill:
        ax.fill(x, y, alpha=alpha, color=fill_color)

with open(in_file_path, 'r') as file:
    geo_data_json = json.load(file)

polygons = []
f_index = 0

geo_data_features = geo_data_json["features"]

for feature in geo_data_features:
    #print("feature: " + str(f_index))
    coordinates = feature["geometry"]["coordinates"][0][0]
    coord_tuples = []
    c_index = 0
    for coordinate in coordinates:
        coord_tuple = ( coordinate[0], coordinate[1] )
        coord_tuples.append(coord_tuple)
        c_index = c_index + 1
        #print(" coordinate: " + str(c_index))
    polygons.append( Polygon(coord_tuples) )
    #print("polygon: " + str(coord_tuples))
    f_index = f_index + 1

union_polygon = unary_union(polygons)
print(union_polygon.geom_type)
print("Input features : ", len(geo_data_features))
print("Output unions  : ", len(union_polygon.geoms))
#print("Union of polygons:", list(union_polygon.exterior.coords))

# Define polygons
#polygon1 = Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])
#polygon2 = Polygon([(1, 1), (3, 1), (3, 3), (1, 3)])
# Compute the union of the two polygons
#union_polygon = unary_union([polygon1, polygon2])
# Print the coordinates of the union polygon
#print("Union of polygon1 and polygon2:", list(union_polygon.exterior.coords))


if show_plot:

   for geom in union_polygon.geoms:
      fig, ax = plt.subplots()
      # Plotting
      # Plot the original polygons
      #plot_polygon(ax, polygon1, color='red', fill=True, fill_color='red', alpha=0.3)
      #plot_polygon(ax, polygon2, color='green', fill=True, fill_color='green', alpha=0.3)

      # Plot the union polygon
      plot_polygon(ax, geom, color='blue', linewidth=2, fill=True, fill_color='blue', alpha=0.3)

      # Setting plot limits
      minx, miny, maxx, maxy = geom.bounds
      ax.set_xlim(minx - 1, maxx + 1)
      ax.set_ylim(miny - 1, maxy + 1)

      # Show plot
      plt.show()


data_out = {
    "type": "FeatureCollection",
    "name": "poly2",
    "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:EPSG::5514" } },
    "features": []
}

for geom in union_polygon.geoms:
    feature = { "type": "Feature", "properties": { }, "geometry": { "type": "MultiPolygon", "coordinates": [[]] }}
    coords = geom.exterior.coords
    coords_array = []
    for coord in coords:
        coord_array = [ coord[0], coord[1] ]
        coords_array.append(coord_array)
    feature["geometry"]["coordinates"][0].append(coords_array)
    data_out["features"].append(feature)

with open(out_file_path, 'w') as file:
    json.dump(data_out, file, indent=4)