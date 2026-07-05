from pathlib import Path

from app.models import (
    VertexProject,
    DateProject,
    RequestProject
)


def choose_excel_file(root: Path):

    excel_files = [
        file
        for file in root.glob("*.xlsx")
        if not file.name.startswith("~$")
    ]

    if len(excel_files) == 0:

        print("\n❌ No Excel file found.")
        return None

    if len(excel_files) == 1:

        print("\nExcel File:")
        print(f"   {excel_files[0].name}")

        return excel_files[0]

    print("\n")
    print("=" * 50)
    print(f"Found {len(excel_files)} Excel Files")
    print("=" * 50)

    for i, file in enumerate(excel_files, start=1):

        print(f"{i}) {file.name}")

    while True:

        try:

            choice = int(input("\nChoose Excel File Number : "))

            if 1 <= choice <= len(excel_files):

                return excel_files[choice - 1]

        except ValueError:
            pass

        print("Invalid choice.")


def scan_vertex(root: Path):

    print("=" * 50)
    print("Scanning Vertex Folder...")
    print("=" * 50)

    project = VertexProject(root=root)

    project.excel_file = choose_excel_file(root)

    if project.excel_file is None:
        return None

    date_folders = sorted(

        [folder for folder in root.iterdir() if folder.is_dir()],

        key=lambda folder: folder.name

    )

    for folder in date_folders:

        date_project = DateProject(

            name=folder.name,

            path=folder

        )

        # ------------------------------------
        # Find Shape Folder
        # ------------------------------------

        for item in folder.iterdir():

            if not item.is_dir():
                continue

            shp_files = list(item.glob("*.shp"))

            if shp_files:

                date_project.shapefile_folder = item

                date_project.shapefile = shp_files[0]

                break

        # ------------------------------------
        # Request Folders
        # ------------------------------------

        request_folders = sorted(

            [
                f
                for f in folder.iterdir()
                if f.is_dir() and f.name.isdigit()
            ],

            key=lambda x: int(x.name)

        )

        for request_folder in request_folders:

            request = RequestProject(

                folder_number=int(request_folder.name),

                folder_path=request_folder,

                request_number=""

            )

            kmz_files = list(request_folder.glob("*.kmz"))

            if kmz_files:
                request.kmz_file = kmz_files[0]

            for item in request_folder.iterdir():

                if item.is_dir():

                    request.image_folder = item

                    request.request_number = item.name

                    request.images = [

                        image

                        for image in item.iterdir()

                        if image.is_file()

                    ]

                    break

            date_project.requests.append(request)

            if request.request_number:
                date_project.request_lookup[request.request_number] = request

        project.date_folders.append(date_project)

    print("\nFinished Scanning.")

    return project