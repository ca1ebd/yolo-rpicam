FROM ultralytics/ultralytics:8.2.30-arm64

RUN apt update && apt install -y --no-install-recommends \
    gnupg \
    vim

RUN echo "deb http://archive.raspberrypi.org/debian/ bookworm main" > /etc/apt/sources.list.d/raspi.list \
  && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 82B129927FA3303E

RUN apt update && apt -y upgrade

RUN apt update && apt install -y --no-install-recommends \
    python3-picamera2

WORKDIR /usr/src/ultralytics
RUN yolo export model=yolov8n.pt format=ncnn
COPY main.py /app/

CMD [ "python3", "/app/main.py" ]


