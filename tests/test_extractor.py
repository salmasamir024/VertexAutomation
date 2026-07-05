from pathlib import Path

from ai.card_reader import CardReader
from ai.extractor import Extractor


reader = CardReader()
extractor = Extractor()

text = reader.read(
    Path("output/cards/card.jpg")
)

print(text)

print()

print("Name")
print(
    extractor.extract_name(text)
)

print()

print("National ID")
print(
    extractor.extract_national_id(text)
)