import shutil
from pathlib import Path

import geopandas as gpd

from app.classifier import FeatureClassifier
from app.shp_exporter import ShpExporter


RESULT_ROOT = Path("result")


class Exporter:

    def __init__(self):

        self.classifier = FeatureClassifier()
        self.shp_exporter = ShpExporter()

    def export(self, project):

        today_folder = RESULT_ROOT / str(project.date_folders[0].name)

        today_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        exported = 0
        missing = 0

        for date in project.date_folders:

            updated = None

            for shp in date.shapefile.parent.glob("*_updated.shp"):
                updated = shp
                break

            if updated is None:

                print(f"No updated shp found in {date.name}")
                continue

            gdf = gpd.read_file(updated)

            for _, row in gdf.iterrows():

                surv_num = str(row["surv_num"]).strip()

                request = date.request_lookup.get(surv_num)

                if request is None:

                    print("Missing Folder :", surv_num)
                    missing += 1
                    continue

                request_folder = today_folder / surv_num

                request_folder.mkdir(
                    parents=True,
                    exist_ok=True
                )

                # --------------------------------
                # Copy Images
                # --------------------------------

                if request.image_folder:

                    for file in request.image_folder.iterdir():

                        if file.is_file():

                            shutil.copy2(
                                file,
                                request_folder / file.name
                            )

                # --------------------------------
                # Export SHP
                # --------------------------------

                filename = self.classifier.get_filename(row)

                self.shp_exporter.export_record(
                    row,
                    request_folder,
                    filename
                )

                exported += 1

        print()
        print("=" * 50)
        print("Export Report")
        print("=" * 50)

        print("Exported :", exported)
        print("Missing :", missing)
        print("Saved To :", today_folder)