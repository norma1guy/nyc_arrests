import pyrosm
import geopandas as gpd
import matplotlib.pyplot as plt

# load PBF
nyc_pbf = pyrosm.get_data("newyorkcity")
osm = pyrosm.OSM(nyc_pbf)

# get boundaries
boundaries = osm.get_boundaries()

# filter for the city you want
nyc_boundary = boundaries[boundaries["name"] == "New York"]

# plot
fig, ax = plt.subplots(figsize=(10,10))

nyc_boundary.plot(ax=ax, facecolor="none", edgecolor="red", linewidth=2)
#roads.plot(ax=ax, color="black", linewidth=0.5)

plt.show()