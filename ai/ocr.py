from surya.detection import DetectionPredictor
from surya.recognition import RecognitionPredictor


class OCR:

    def __init__(self):

        print("Loading Surya...")

        self.detector = DetectionPredictor()
        self.recognizer = RecognitionPredictor()

        print("Surya Ready")

    def read(self, image):

        detections = self.detector([image])

        predictions = self.recognizer(
            [image],
            detections
        )

        text = []

        for page in predictions:
            for line in page.text_lines:
                text.append(line.text)

        return " ".join(text)