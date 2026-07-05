import geopandas as gpd


def update_shapefile(date_project):

    print("\n")
    print("=" * 50)
    print(f"Updating {date_project.name}")
    print("=" * 50)

    gdf = gpd.read_file(date_project.shapefile)

    updated = 0
    missing = 0

    for index, row in gdf.iterrows():

        surv_num = str(row["surv_num"]).strip()

        # ابحث عن الطلب داخل المشروع
        request = date_project.request_lookup.get(surv_num)

        if request is None or request.excel is None:

            print(f"Not Found : {surv_num}")

            missing += 1
            continue

        excel = request.excel

        # تحديث الحقول
        gdf.at[index, "request_nu"] = excel.request_nu
        gdf.at[index, "name"] = excel.owner
        gdf.at[index, "company"] = excel.company
        gdf.at[index, "gov"] = excel.gov
        gdf.at[index, "sec"] = excel.sec
        gdf.at[index, "location"] = excel.location
        gdf.at[index, "النوع"] = excel.request_type

        updated += 1

    output_file = (
        date_project.shapefile.parent /
        f"{date_project.shapefile.stem}_updated.shp"
    )

    gdf.to_file(
        output_file,
        driver="ESRI Shapefile",
        encoding="utf-8"
    )

    print("\n")
    print("=" * 50)
    print("Update Report")
    print("=" * 50)

    print(f"Updated : {updated}")
    print(f"Missing : {missing}")

    print(f"\nSaved To:\n{output_file}")