from pathlib import Path

import torch
from PIL import Image

from transformers import AutoProcessor
from transformers import AutoModelForZeroShotObjectDetection


class CardDetector:

    def __init__(self):

        print("Loading Grounding DINO...")

        self.device = (
            "cuda"
            if torch.cuda.is_available()
            else "cpu"
        )

        self.processor = AutoProcessor.from_pretrained(
            "IDEA-Research/grounding-dino-base"
        )

        self.model = (
            AutoModelForZeroShotObjectDetection
            .from_pretrained(
                "IDEA-Research/grounding-dino-base"
            )
            .to(self.device)
        )

        print("Grounding DINO Ready.")

    def detect(self, image_path: Path):

        image = Image.open(image_path).convert("RGB")

        text = "identity card."

        inputs = self.processor(
            images=image,
            text=text,
            return_tensors="pt"
        ).to(self.device)

        with torch.no_grad():

            outputs = self.model(**inputs)

        results = self.processor.post_process_grounded_object_detection(
            outputs,
            inputs.input_ids,
            threshold=0.30,
            text_threshold=0.25,
            target_sizes=[image.size[::-1]]
        )[0]

        return image, results