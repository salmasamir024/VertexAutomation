from dataclasses import dataclass, field
from pathlib import Path


# ==========================================
# Excel Record
# ==========================================

@dataclass
class ExcelRequest:

    surv_num: str
    request_nu: str

    gov: str
    sec: str
    location: str

    area: float

    request_type: str

    request_date: str

    owner: str

    phone: str

    company: str

    survey_status: str

    geodesy_status: str

    inspection_status: str

    national_id: str = ""

    land_description: str = ""

    building_description: str = ""


# ==========================================
# One Request Folder
# ==========================================

@dataclass
class RequestProject:

    folder_number: int

    folder_path: Path

    request_number: str

    kmz_file: Path | None = None

    image_folder: Path | None = None

    images: list[Path] = field(default_factory=list)

    excel: "ExcelRequest | None" = None

    ocr: "CardData | None" = None


# ==========================================
# One Date Folder
# ==========================================

@dataclass
class DateProject:

    name: str

    path: Path

    shapefile_folder: Path | None = None

    shapefile: Path | None = None

    requests: list[RequestProject] = field(default_factory=list)

    request_lookup: dict[str, RequestProject] = field(default_factory=dict)


# ==========================================
# Whole Vertex Project
# ==========================================

@dataclass
class VertexProject:

    root: Path

    excel_file: Path | None = None

    excel_database: dict[str, ExcelRequest] = field(default_factory=dict)

    date_folders: list[DateProject] = field(default_factory=list)


@dataclass
class CardData:

    national_id: str | None = None

    name: str | None = None

    confidence: float = 0.0

    image = None