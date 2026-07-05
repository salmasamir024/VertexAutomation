from doctr.io import DocumentFile
from doctr.models import kie_predictor

model = kie_predictor(
    det_arch="db_resnet50",
    reco_arch="crnn_vgg16_bn",
    pretrained=True
)

doc = DocumentFile.from_images("test_images/WhatsApp Image 2026-06-07 at 3.48.51 PM.jpeg")

result = model(doc)

print(result.render())