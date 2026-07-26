from picamera2 import Picamera2
from edge_impulse_linux.image import ImageImpulseRunner
import cv2
import time
from datetime import datetime
from picamera2.encoders import H264Encoder

MODEL_PATH = "model/model.eim"
CONFIDENCE_THRESHOLD = 0.75
VIDEO_CONFIDENCE_THRESHOLD = 0.90

RECORDING_COOLDOWN = 10
last_recording_time = 0

runner = ImageImpulseRunner(MODEL_PATH)
model_info = runner.init()
print("Model loaded. Labels: ", model_info["model_parameters"]["labels"])

picam2 = Picamera2()
config = picam2.create_preview_configuration(
    main={"size": (640, 480), "format": "RGB888"}
)

picam2.configure(config)
picam2.start()

time.sleep(2)
print("Running live detector. Press q to quit.")

while True:
    frame = picam2.capture_array()

    features, cropped_frame = runner.get_features_from_image(frame)
    result = runner.classify(features)

    predictions = result["result"]["classification"]
    best_label = max(predictions, key=predictions.get)
    confidence = predictions[best_label]

    text = f"{best_label}: {confidence:.2f}"
    
    current_time = time.time()

    if confidence >= CONFIDENCE_THRESHOLD:
        display_text = text
    else:
            display_text = "Not Certain"
    
    if (
        confidence >= VIDEO_CONFIDENCE_THRESHOLD 
        and best_label == "oliver"
        and current_time - last_recording_time >= RECORDING_COOLDOWN
        ):

        display_text = text

        #Gives the filename a timestamp
        filename = datetime.now().strftime(
            "videos/cat_%Y%m%d_%H%M%S.mp4"
        )

        picam2.start_recording(H264Encoder(), filename)
        time.sleep(5)
        picam2.stop_recording()

        last_recording_time = time.time()

    #Convert RGB to BGR for rendering
    #or else red and blue channels will be swapped
    display_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    cv2.putText(
        frame,
        display_text,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2,
    )

    cv2.imshow("Oliver Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

picam2.stop()
runner.stop()
cv2.destroyAllWindows()