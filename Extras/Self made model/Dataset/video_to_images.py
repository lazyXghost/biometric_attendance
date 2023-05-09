import cv2
import os
import sys

if len(sys.argv) < 3:
    print("Usage python3 <script_name> <video_name> <final_dir_path>")
    exit()

file = sys.argv[1]
output_folder = sys.argv[2]

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
cap = cv2.VideoCapture(file)
os.makedirs(output_folder, exist_ok=True)
frame_count = 0
while True:
    ret, img_bgr = cap.read()
    if not ret:
        break
    frame_count += 1

    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=5, minSize=(110, 110))
    try:
        for i, (x, y, w, h) in enumerate(faces):
            img_bgr = img_bgr[y:y+h,x:x+w]
            img_bgr = cv2.resize(img_bgr, (600, 600))
            cv2.imwrite(output_folder + "/" + f'frame_{frame_count}.jpg', img_bgr) 
    except:
        print("error")
