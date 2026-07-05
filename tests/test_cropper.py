from pathlib import Path

from ai.detector import CardDetector
from ai.cropper import CardCropper

image_path = Path(
    "test_images/A-B28-2801-02-00000133556/WhatsApp Image 2026-06-07 at 12.50.26 PM.jpeg"
)

detector = CardDetector()

image, detection = detector.detect(image_path)

cropper = CardCropper()

output = cropper.crop(
    image,
    detection,
    Path("output/cards/card.jpg")
)

print()

print("=" * 50)
print("Saved")
print("=" * 50)

print(output)