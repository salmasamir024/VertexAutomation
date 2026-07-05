import cv2

from ai.preprocess import Preprocessor
from ai.regions import Regions
from ai.ocr import OCR


image = cv2.imread("output/cards/card.jpg")

pre = Preprocessor()
image = pre.process(image)

regions = Regions()

name_img, id_img = regions.extract(image)

ocr = OCR()

print("\n================ NAME ================\n")
print(ocr.read(name_img))

print("\n================ ID ================\n")
print(ocr.read(id_img))

cv2.imshow("Name", name_img)
cv2.imshow("ID", id_img)

cv2.waitKey(0)
cv2.destroyAllWindows()