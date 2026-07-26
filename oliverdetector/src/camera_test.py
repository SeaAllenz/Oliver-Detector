from picamera2 import Picamera2, Preview
import time

picam2 = Picamera2()
picam2.start_preview(Preview.QTGL)
picam2.start()

print("Camera preview running for 10 seconds...")
time.sleep(10)

picam2.stop()