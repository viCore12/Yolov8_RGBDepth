from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")

model.predict("datasets/data/train_stereo/images/36.jpg", save=True, conf=0.1)