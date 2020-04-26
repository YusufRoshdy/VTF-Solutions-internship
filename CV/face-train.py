import os
import numpy as np
import cv2
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, 'images')


face_cascade = cv2.CascadeClassifier('cascades\data\haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

current_id = 0
lable_ids = {}
y_lables = []
x_train = []

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            lable = os.path.basename(root).replace(' ', '-').lower()
            if lable not in lable_ids:
                lable_ids[lable] = current_id
                current_id += 1
            id_ = lable_ids[lable]


            image_array = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            size = (512,512)
            final_image = cv2.resize(image_array, size, interpolation = cv2.INTER_AREA)
            faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)
            for (x,y,w,h) in faces:
                roi = image_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_lables.append(id_)
        
with open("lables.pickle", 'wb') as f:
    pickle.dump(lable_ids, f) 

recognizer.train(x_train, np.array(y_lables))
recognizer.save("trainner.yml")