import geopandas as gp
import os
gdf = gp.read_file("RiverHRCenterlinesCombo/RiverHRCenterlinesCombo.shp")
gdf = gdf[gdf.NAME == "Mississippi"]
gdf.plot()


