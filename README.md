# Yolov8-RGBDepth
## Train on your custom data
```rb
from ultralytics import YOLO
import torch

model = YOLO("yolov8n.pt") 
model.train(data="/content/drive/MyDrive/data/mydataset.yaml", epochs=20, batch=8, device='cuda:0')
```


