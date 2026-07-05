from pathlib import Path

from ai.preprocess import ImagePreprocessor


processor = ImagePreprocessor()

output = processor.preprocess(

    Path("output/cards/card.jpg"),

    Path("output/cards/card_processed.jpg")

)

print()

print("=" * 50)
print("Processed")
print("=" * 50)

print(output)