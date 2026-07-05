from pathlib import Path
import cv2


VALID_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png"
}


def is_image(path: Path):

    return path.suffix.lower() in VALID_EXTENSIONS


def load_image(path: Path):

    return cv2.imread(str(path))