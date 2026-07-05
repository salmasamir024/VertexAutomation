import cv2

from ai.regions import Regions

image = cv2.imread("output/cards/card.jpg")

regions = Regions().extract(image)

for name, img in regions.items():

    cv2.imwrite(f"output/{name}.jpg", img)

    print(name, img.shape)