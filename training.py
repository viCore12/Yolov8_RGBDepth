from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model.train(data="datasets/data/mydataset.yaml", epochs=1, batch=8, workers=4)