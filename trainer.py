import cv2
import os
import numpy as np

print(cv2.__version__)

# path to the dataset
dataset_path = 'TrainingImages'

# initialize the recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# create a list to store faces and labels
faces = []
labels = []

# loop through all folders and images in the dataset path
for folder_name in os.listdir(dataset_path):
    folder_path = os.path.join(dataset_path, folder_name)
    if not os.path.isdir(folder_path):
        continue
    
    label = int(list(word[0] for word in folder_name.split())[0])
    
    # loop through all images in the folder
    for file_name in os.listdir(folder_path):
        image_path = os.path.join(folder_path, file_name)
        if not os.path.isfile(image_path):
            continue
        try:

            # read the image and convert it to grayscale
            image = cv2.imread(image_path)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            print(f"image read: {image_path}")

        except: 
            print(f"Could not read image: {image_path}")
            continue

        # detect faces in the image
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        faces_rect = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
        
        # loop through all detected faces and add them to the list of faces
        for (x, y, w, h) in faces_rect:
            faces.append(gray[y:y+h, x:x+w])
            labels.append(label)

# train the recognizer with the faces and labels
recognizer.train(faces, np.array(labels))

# save the trained recognizer to a file
recognizer.save('trained_data.yml')
