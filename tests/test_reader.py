from pathlib import Path

from ai.card_reader import CardReader


reader = CardReader()

text = reader.read(
    Path("output/cards/card.jpg")
)

print()

print("=" * 50)
print("CARD TEXT")
print("=" * 50)

print(text)