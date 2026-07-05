import customtkinter as ctk


class DateCard(ctk.CTkFrame):

    def __init__(self, master, project):

        super().__init__(
            master,
            corner_radius=15
        )

        self.project = project

        self.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(

            self,

            text=f"📅 {project.name}",

            font=("Segoe UI", 22, "bold")

        )

        title.grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=(15,5)
        )

        requests = len(project.requests)

        ctk.CTkLabel(

            self,

            text=f"Requests : {requests}",

            font=("Segoe UI",16)

        ).grid(

            row=1,
            column=0,
            sticky="w",
            padx=20

        )

        shp = "✔" if project.shapefile else "✖"

        ctk.CTkLabel(

            self,

            text=f"Shape : {shp}",

            font=("Segoe UI",16)

        ).grid(

            row=2,
            column=0,
            sticky="w",
            padx=20

        )

        button = ctk.CTkButton(

            self,

            text="Open",

            width=150,

            command=self.open_project

        )

        button.grid(

            row=0,

            column=1,

            rowspan=3,

            padx=20

        )

    def open_project(self):

        self.master.master.show_dashboard(
            self.project
        )