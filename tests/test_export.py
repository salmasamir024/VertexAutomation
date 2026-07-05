from pathlib import Path

from app.pipeline import Pipeline
from app.scanner import scan_vertex


vertex = Path(r"E:\Work\Vertex")

project = scan_vertex(vertex)

if project is None:
    exit()

Pipeline().run(project)