import os
import customtkinter as ctk

from app.exporter import Exporter
from app.gis import update_shapefile


class Dashboard(ctk.CTkFrame):

    def __init__(self, master, date_project):

        super().__init__(master)

        self.date_project = date_project

        # ==========================
        # Title
        # ==========================

        title = ctk.CTkLabel(

            self,

            text=f"📅 {date_project.name}",

            font=("Segoe UI", 28, "bold")

        )

        title.pack(
            pady=20
        )

        # ==========================
        # Information
        # ==========================

        info = ctk.CTkFrame(self)

        info.pack(
            fill="x",
            padx=40,
            pady=20
        )

        labels = [

            ("Requests", len(date_project.requests)),

            (
                "Shapefile",
                date_project.shapefile.name
                if date_project.shapefile
                else "Not Found"
            ),

            ("Folder", date_project.path.name)

        ]

        for text, value in labels:

            row = ctk.CTkFrame(info)

            row.pack(
                fill="x",
                padx=15,
                pady=5
            )

            ctk.CTkLabel(

                row,

                text=text,

                width=120,

                anchor="w",

                font=("Segoe UI", 16, "bold")

            ).pack(side="left")

            ctk.CTkLabel(

                row,

                text=str(value),

                anchor="w",

                font=("Segoe UI", 16)

            ).pack(side="left")

        # ==========================
        # Buttons
        # ==========================

        buttons = ctk.CTkFrame(self)

        buttons.pack(
            pady=20
        )

        ctk.CTkButton(

            buttons,

            text="Update SHP",

            width=220,

            command=self.update_shp

        ).pack(
            pady=8
        )

        ctk.CTkButton(

            buttons,

            text="Export Result",

            width=220,

            command=self.export

        ).pack(
            pady=8
        )

        ctk.CTkButton(

            buttons,

            text="Open Result Folder",

            width=220,

            command=self.open_result

        ).pack(
            pady=8
        )

        ctk.CTkButton(

            buttons,

            text="Open Source Folder",

            width=220,

            command=self.open_source

        ).pack(
            pady=8
        )

        ctk.CTkButton(

            buttons,

            text="Open SHP Folder",

            width=220,

            command=self.open_shp

        ).pack(
            pady=8
        )

        ctk.CTkButton(

            buttons,

            text="OCR (Coming Soon)",

            width=220,

            state="disabled"

        ).pack(
            pady=8
        )

        # ==========================
        # Back
        # ==========================

        ctk.CTkButton(

            self,

            text="← Back",

            width=220,

            command=master.show_home

        ).pack(
            pady=30
        )

    # ==========================================================
    # Actions
    # ==========================================================

    def update_shp(self):

        update_shapefile(self.date_project)

        print("Update Finished.")

    def export(self):

        exporter = Exporter()

        exporter.export(self.date_project)

        print("Export Finished.")

    def open_result(self):

        result_folder = os.path.join(
            "result",
            self.date_project.name
        )

        if os.path.exists(result_folder):
            os.startfile(result_folder)

    def open_source(self):

        os.startfile(self.date_project.path)

    def open_shp(self):

        if self.date_project.shapefile:

            os.startfile(
                self.date_project.shapefile.parent
            )