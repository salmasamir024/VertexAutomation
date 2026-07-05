import cv2


class Regions:

    def extract(self, image):

        h, w = image.shape[:2]

        # ==========================
        # Name Region
        # ==========================

        padding = int(w * 0.03)

        x1 = max(0, int(w * 0.18) - padding)
        x2 = min(w, int(w * 0.92) + padding)

        y1 = max(0, int(h * 0.25) - 10)
        y2 = min(h, int(h * 0.50) + 10)

        name = image[y1:y2, x1:x2]

        # ==========================
        # National ID Region
        # ==========================

        padding = int(w * 0.03)

        x1 = max(0, int(w * 0.30) - padding)
        x2 = min(w, int(w * 0.95) + padding)

        y1 = max(0, int(h * 0.68) - 10)
        y2 = min(h, int(h * 0.88) + 10)

        national_id = image[y1:y2, x1:x2]

        return name, national_id