from pathlib import Path

from ai.card_selector import CardSelector

folder = Path(
    "test_images/A-B28-2801-02-00000133556"
)

selector = CardSelector()

cards = selector.select(folder)

print()

print("=" * 50)
print("Candidates")
print("=" * 50)

for score, image in cards:

    print(image.name)
    print(score)
    print()