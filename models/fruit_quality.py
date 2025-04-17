from fastapi import HTTPException
import numpy as np
import tensorflow as tf
import cv2
import os

class FruitQualityModel:
    def __init__(self):
        self.image_size = 224
        self.dataset_path = r'D:\DP\DesignProject\models\fruits_quality_classification\dataset'  # parth Change this path accordingly to your system 
        self.model_path = r'D:\DP\DesignProject\models\fruits_quality_classification\leaf_model_mobilenetv2.h5'
        self.class_names = sorted(os.listdir(self.dataset_path)) 

        try:
            self.model = tf.keras.models.load_model(self.model_path)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error loading model: {str(e)}")
    
    def predict_image(self, image_path):
        try:
            img = cv2.imread(image_path)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error reading image: {str(e)}")
        
        if img is None:
            raise HTTPException(status_code=400, detail="Image not found or invalid image format")
        
        try:
            img = cv2.resize(img, (self.image_size, self.image_size))
            img = img.astype('float32') / 255.0
            img = np.expand_dims(img, axis=0)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")
        
        try:
            predictions = self.model.predict(img)
            predicted_class_index = int(np.argmax(predictions, axis=1)[0])
            predicted_class = self.class_names[predicted_class_index]
            confidence = float(np.max(predictions)) * 100
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error during prediction: {str(e)}")
        
        return {
            "predicted_class": predicted_class,
            "confidence": confidence
        }

