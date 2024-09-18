# Yolov8-RGBDepth


## Train on your custom data
```rb
from ultralytics import YOLO
import torch

model = YOLO("yolov8n.pt") 
model.train(data="/content/drive/MyDrive/data/mydataset.yaml", epochs=20, batch=8, device='cuda:0')
```
## Generate depth map using intel-isl/MiDaS
depth_model = torch.hub.load("intel-isl/MiDaS", "MiDaS_small")
depth_transform = torch.hub.load("intel-isl/MiDaS", "transforms").small_transform


