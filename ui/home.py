from pathlib import Path

import customtkinter as ctk

from app.scanner import scan_vertex

from ui.widgets import DateCard


class HomePage(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        title = ctk.CTkLabel(

            self,

            text="Vertex Automation",

            font=("Segoe UI",30,"bold")

        )

        title.pack(
            pady=20
        )

        root = Path(r"E:\Work\Vertex")

        self.project = scan_vertex(root)

        for date in self.project.date_folders:

            card = DateCard(

                self,

                date

            )

            card.pack(

                fill="x",

                padx=40,

                pady=10

            )