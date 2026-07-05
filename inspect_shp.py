import geopandas as gpd

gdf = gpd.read_file(r"E:\Work\Vertex\7-6-2026\اسوان7-6-2026\اسوان_21.shp")

print("\nFields:\n")

for col in gdf.columns:
    print(col)