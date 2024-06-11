# yolo-rpicam

This project makes it easier to use the YOLO models on a Raspberry Pi with a live video feed from the Raspberry Pi Camera.

The container is based on the ultralytics YOLOv8 container, and then install picamera2 on top. This project also converts the model to the NCNN format, which is the most performant on Raspberry Pi.

See [docker-compose.yml](docker-compose.yml) to see arguments.

## Attributions

This project builds on the following projects:
-  [Ultralytics YOLOv8 ](https://github.com/ultralytics/ultralytics)
-  [pi-camera-in-docker](https://github.com/hyzhak/pi-camera-in-docker/blob/main/README.md) 
