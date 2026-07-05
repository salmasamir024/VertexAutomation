from pathlib import Path

import geopandas as gpd


class ShpExporter:

    def export_record(
        self,
        row,
        output_folder: Path,
        filename: str
    ):

        shp_folder = output_folder / "shp"

        shp_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        gdf = gpd.GeoDataFrame(
            [row],
            geometry="geometry",
            crs="EPSG:32636"
        )

        output = shp_folder / f"{filename}.shp"

        gdf.to_file(
            output,
            driver="ESRI Shapefile",
            encoding="utf-8"
        )

        return output