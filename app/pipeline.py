from app.exporter import Exporter


class Pipeline:

    def __init__(self):

        self.exporter = Exporter()

    def run(self, project):

        print()
        print("=" * 50)
        print("EXPORT RESULT")
        print("=" * 50)

        self.exporter.export(project)

        print()
        print("Finished.")