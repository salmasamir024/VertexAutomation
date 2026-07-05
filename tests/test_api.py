from transformers import AutoProcessor

processor = AutoProcessor.from_pretrained(
    "IDEA-Research/grounding-dino-base"
)

import inspect

print(inspect.signature(
    processor.post_process_grounded_object_detection
))