from pathlib import Path

from ai.detector import CardDetector

image = Path(
    "test_images/A-B28-2801-02-00000133556/WhatsApp Image 2026-06-07 at 12.50.26 PM.jpeg"
)

detector = CardDetector()

image, result = detector.detect(image)

print()

print("=" * 50)
print("Detection")
print("=" * 50)

print(result)


print()

print("=" * 50)
print("BOXES")
print("=" * 50)

print(result["boxes"])

print()

print("=" * 50)
print("SCORES")
print("=" * 50)

print(result["scores"])

print()

print("=" * 50)
print("LABELS")
print("=" * 50)

print(result["labels"])