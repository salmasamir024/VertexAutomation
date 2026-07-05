from pathlib import Path

import cv2


class ImagePreprocessor:

    def preprocess(self, image_path: Path, output_path: Path):

        image = cv2.imread(str(image_path))

        if image is None:
            return None

        # تكبير الصورة
        image = cv2.resize(
            image,
            None,
            fx=2,
            fy=2,
            interpolation=cv2.INTER_CUBIC
        )

        # تحويل لـ Gray
        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

        # تحسين التباين بشكل خفيف
        clahe = cv2.createCLAHE(
            clipLimit=1.5,
            tileGridSize=(8, 8)
        )

        gray = clahe.apply(gray)

        # إزالة Noise بدون تشويه الحروف
        gray = cv2.bilateralFilter(
            gray,
            7,
            50,
            50
        )

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        cv2.imwrite(
            str(output_path),
            gray
        )

        return output_path