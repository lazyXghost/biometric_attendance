from flask import Flask, request, jsonify
import cv2
import numpy as np
import json
from tensorflow import keras

cascPath = "Dataset/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

app = Flask(__name__)

# model = keras.models.load_model('spoofingdetectormodel_hsv_eyeBrows_smallData.h5')
# def preprocess(img):
#     img_eye_eyebrows = cv2.resize(img, (600, 600))[80:310, 60:500]
#     img_hsv = cv2.cvtColor(img_eye_eyebrows, cv2.COLOR_BGR2HSV)
#     hue_channel, _, _ = cv2.split(img_hsv)
#     img_hsv_eye_eyebrows = cv2.normalize(
#         hue_channel, None, 0, 255, cv2.NORM_MINMAX)
#     img_hsv_eye_eyebrows = cv2.resize(
#         img_hsv_eye_eyebrows, (300, 300)).reshape(1, 300, 300, 1)
#     return img_hsv_eye_eyebrows
model = keras.models.load_model('spoofingdetectormodel_hsv_fullFace_largeData.h5')
def preprocess(img):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hue_channel, _, _ = cv2.split(img_hsv)
    img_hue = cv2.normalize(hue_channel, None, 0, 255, cv2.NORM_MINMAX)
    return cv2.resize(img_hue, (300, 300)).reshape(1, 300, 300)


def predictSpoofing(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        img_gray, scaleFactor=1.1, minNeighbors=5, minSize=(110, 110))
    if len(faces):
        (x, y, w, h) = faces[0]
        img_face = img[y:y+h, x:x+w]
        pred = model.predict(preprocess(img_face))
        print(pred)
        if np.argmax(pred) == 0:
            return "Spoofed"
        return "Real"
    return "No face detected"


@app.route('/predict', methods=['POST'])
def predict():
    img = np.array(json.loads(request.json), dtype=np.uint8)
    return (jsonify(predictSpoofing(img)))


if __name__ == '__main__':
    app.run(debug=True)
