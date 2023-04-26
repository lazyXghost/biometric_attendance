import requests
import cv2
import json
import numpy as np

url = 'http://localhost:5000/predict'
image = cv2.imread('Dataset/val_spoofed.jpeg')
image_array = np.array(image)
image_json = json.dumps(image_array.tolist())
headers = {'Content-Type': 'application/json'}
response = requests.post(url, headers=headers, json=image_json)
print(response.json())
