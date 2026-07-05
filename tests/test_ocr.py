from pathlib import Path

from ai.ocr import OCR


ocr = OCR()

text = ocr.read(
    Path("output/cards/card.jpg")
)

print()
print("=" * 50)
print("OCR RESULT")
print("=" * 50)
print(text)