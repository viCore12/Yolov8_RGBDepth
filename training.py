from ultralytics import YOLO

model = YOLO("ckp/last.pt")
model.train(data="datasets/data/overhead.yaml", epochs=6, batch=8, workers=4, pretrained=True)