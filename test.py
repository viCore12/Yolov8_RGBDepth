from ultralytics import YOLO

model = YOLO("ckp/best.pt")

#model.predict("datasets/data/train/images/frame_22861.jpg", save=True, imgsz=640, conf=0.1)
model.predict("datasets/data/train_overhead/images/VID_20210401_130453735-0114_jpg.rf.4ec03db3986103e5f6b1f676079e7801.jpg", save=True, imgsz=640, conf=0.1)
#model.predict(["datasets/data/val/images/frame_1253.jpg", "datasets/data/val/images/frame_1266.jpg"], save=True, imgsz=640, conf=0.5, device='cuda:0')