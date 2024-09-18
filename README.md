# Yolov8-RGBDepth


## Train on your custom data
```rb
from ultralytics import YOLO
import torch

model = YOLO("yolov8n.pt") 
model.train(data="/content/drive/MyDrive/data/mydataset.yaml", epochs=20, batch=8, device='cuda:0')
```
### Generate depth map using intel-isl/MiDaS
```rb
depth_model = torch.hub.load("intel-isl/MiDaS", "MiDaS_small")
depth_transform = torch.hub.load("intel-isl/MiDaS", "transforms").small_transform
```
### Visualize Original image - 4D RGBD image - Depth map image 
![image](https://github.com/user-attachments/assets/70d68ba1-7fa6-494b-bfd4-4dab5d1df291)



