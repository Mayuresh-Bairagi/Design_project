from ultralytics import YOLO
import cv2
import numpy as np

class FruitCounter:
    def __init__(self, model_path=r'models\yolov8n.pt'):
        self.model = YOLO(model_path)
        self.class_names = self.model.names
        self.fruit_class_ids = [47, 49, 50, 51, 52]  

    def load_image(self, image_path):
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError(f"Could not load image from {image_path}")
        return img

    def count_fruits(self, img_or_path, conf_threshold=0.3, filter_fruits=False):

        if isinstance(img_or_path, str):
            img = self.load_image(img_or_path)
        else:
            img = img_or_path.copy()
            if len(img.shape) == 3 and img.shape[2] == 3:
                if img.dtype != np.uint8:
                    img = np.clip(img * 255, 0, 255).astype(np.uint8)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results = self.model(img, conf=conf_threshold)[0]
        boxes = results.boxes
        object_counts = {}
        total_count = 0

        for class_id in range(len(self.class_names)):
            count = sum(1 for box in boxes if int(box.cls.item()) == class_id)
            if count > 0:
                if filter_fruits and class_id not in self.fruit_class_ids:
                    continue
                class_name = self.class_names[class_id]
                object_counts[class_name] = count
                total_count += count

        object_counts['total'] = total_count
        return object_counts
