import cv2
from datetime import datetime
from picamera2 import Picamera2
from ultralytics import YOLO
import os

# Initialize the Picamera2
picam2 = Picamera2()
picam2.preview_configuration.main.size = (1280, 720)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

# Load the YOLOv8 model
model = YOLO("/usr/src/ultralytics/yolov8n_ncnn_model")

# Get the current date and time
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

# Create the output folder with the timestamp
output_folder = f"output_frames_{timestamp}"
output_path = os.path.join("/output", output_folder)
os.makedirs(output_path, exist_ok=True)

frame_count = 0

while True:
    # Capture frame-by-frame
    frame = picam2.capture_array()

    # Run YOLOv8 inference on the frame
    results = model(frame)

    # Visualize the results on the frame
    annotated_frame = results[0].plot()

    # Display the resulting frame
    #cv2.imshow("Camera", annotated_frame)

    # Save the frame to the output folder
    frame_path = os.path.join(output_path, f"frame_{frame_count}.jpg")
    cv2.imwrite(frame_path, annotated_frame)
    frame_count += 1

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord("q"):
        break

# Release resources and close windows
cv2.destroyAllWindows()

