from ultralytics import YOLO

model = YOLO("ckp/yolov8m.pt")
model.train(data="datasets/data/mydataset.yaml", depth_data="datasets/data/depthmap.yaml", epochs=400, batch=8, workers=4, pretrained=False)