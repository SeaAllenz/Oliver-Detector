from edge_impulse_linux.image import ImageImpulseRunner

MODEL_PATH = "model/model.eim"

runner = ImageImpulseRunner(MODEL_PATH)
model_info = runner.init()

print("Model loaded!")
print("Labels:", model_info["model_parameters"]["labels"])

runner.stop()