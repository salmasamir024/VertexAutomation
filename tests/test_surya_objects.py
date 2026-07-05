from PIL import Image
from surya.detection import DetectionPredictor

image = Image.open("output/id.jpg").convert("RGB")

detector = DetectionPredictor()

boxes = detector([image])

print(type(boxes))
print()

print(type(boxes[0]))
print()

print(boxes[0])

print()

print(dir(boxes[0]))