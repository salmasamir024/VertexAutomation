from surya.recognition import RecognitionPredictor
import inspect

model = RecognitionPredictor()

print(dir(model))
print(inspect.signature(model.__call__))