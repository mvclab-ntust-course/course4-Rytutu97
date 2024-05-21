!pip install ultralytics
!pip install opencv-python-headless
!pip install moviepy

!wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1MLEVXG0PTIjwem5DKbTDGaRu7QYoIE6m' -O argoverse_video.mp4

from ultralytics import YOLO


model = YOLO('yolov8n.pt')


results = model.track(source='argoverse_video.mp4', save=True, classes=[2])