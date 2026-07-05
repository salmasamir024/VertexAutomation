from pathlib import Path

import cv2
import numpy as np


class CardCropper:

    def crop(self, image, detection, output_path: Path):

        boxes = detection["boxes"]

        if len(boxes) == 0:
            return None

        # أعلى Score
        box = boxes[0].cpu().numpy()

        x1, y1, x2, y2 = box.astype(int)

        image = np.array(image)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        crop = image[y1:y2, x1:x2]

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        cv2.imwrite(
            str(output_path),
            crop
        )

        return output_path