from pathlib import Path

from ai.preprocess import ImagePreprocessor
from ai.ocr import OCR


class CardReader:

    def __init__(self):

        self.preprocessor = ImagePreprocessor()
        self.ocr = OCR()

    def read(self, card_image: Path):

        processed = Path("output/cards/card_processed.jpg")

        self.preprocessor.preprocess(
            card_image,
            processed
        )

        text = self.ocr.read(processed)

        return text