from pathlib import Path

from app.scanner import scan_vertex
from app.excel_reader import read_excel
from app.database import build_request_database
from app.gis import update_shapefile
from app.linker import link_requests
from app.vision import load_image
# from app.ocr import process_request


vertex_folder = Path(r"E:\Work\Vertex")

project = scan_vertex(vertex_folder)

if project is None:
    exit()

df = read_excel(project.excel_file)

project.excel_database = build_request_database(df)

link_requests(project)

from app.gis import update_shapefile

for date in project.date_folders:

    update_shapefile(date)

print()
print("=" * 50)
print("OCR")
print("=" * 50)

for date in project.date_folders:

    for request in date.requests:

        ok = process_request(request)

        if ok:

            print(

                request.request_number,

                request.ocr["national_id"]

            )

        else:

            print(

                request.request_number,

                "No ID Found"

            )

print()

print("=" * 50)

print("Project Summary")

print("=" * 50)

print(f"Excel : {project.excel_file.name}")

print(f"Date Folders : {len(project.date_folders)}")

for date in project.date_folders:

    print()

    print(date.name)

    print(f"Shape : {date.shapefile.name}")

    print(f"Requests : {len(date.requests)}")

print("\n")
print("=" * 50)
print("Requests")
print("=" * 50)

for date in project.date_folders:

    for request in date.requests:

        print("---------------------------")

        print("Folder :", request.folder_number)

        print("Request :", request.request_number)

        print("KMZ :", request.kmz_file.name)

        print("Images :", len(request.images))


first = project.date_folders[0].requests[0]

print(first.request_number)

print(first.excel.owner)

print(first.excel.phone)


first = project.date_folders[0].requests[0]

for image in first.images:

    img = load_image(image)

    if img is None:
        print(image.name, "FAILED TO LOAD IMAGE")
        continue

    print(image.name, img.shape)