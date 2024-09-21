# Yolov8_RGBDepth
The ultralytics framework customed to training data with 4D input. Link: https://docs.ultralytics.com/
$ ./tree-md .
### Project tree
 * [datasets](./datasets)
   * [data](./datasets/data)
     * [train](./datasets/data/train)
       * [images](./datasets/data/train/images)
         * [image_001.png](./datasets/data/train/images/image_001.png)
         * [...]
       * [labels](./datasets/data/labels/labels)
         * [label_001.txt](./datasets/data/train/labels/label_001.txt)
         * [...]
     * [val](./dir2/file23.ext)
       * [images](./datasets/data/val/images)
         * [image_001.png](./datasets/data/val/images/image_001.png)
         * [...]
       * [labels](./datasets/data/labels/labels)
         * [label_001.txt](./datasets/data/val/labels/label_001.txt)
         * [...]
     * [mydataset.yaml](./datasets/data/mydataset.yaml)
 * [docs](./docs)
 * [test](./test)
 * [ultralytics](./ultralytics)
 * [yolov8m.pt](./yolov8m.pt)
 * [training.py](./training.py)
 * [README.md](./README.md)

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
### Visualize Original image - 4D RGBD image (Original + Depth map) - Depth map image 
![image](https://github.com/user-attachments/assets/70d68ba1-7fa6-494b-bfd4-4dab5d1df291)



