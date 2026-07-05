import customtkinter as ctk

from ui.home import HomePage

from ui.dashboard import Dashboard

from ui.theme import *


class VertexApp(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("Vertex Automation")

        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        self.current = None

        self.show_home()

    def clear(self):

        if self.current:

            self.current.destroy()

    def show_home(self):

        self.clear()

        self.current = HomePage(self)

        self.current.pack(
            fill="both",
            expand=True
        )

    def show_dashboard(self, date_project):

        self.clear()

        self.current = Dashboard(

            self,

            date_project

        )

        self.current.pack(

            fill="both",

            expand=True

        )


app = VertexApp()

app.mainloop()