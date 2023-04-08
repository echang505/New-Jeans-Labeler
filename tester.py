import cv2
import os
import numpy as np

# Load the saved model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trained_data.yml')

# Load the test images
test_dir = 'StructuredTestingImages'
test_images = []
test_labels = []

for filename in os.listdir(test_dir):
    print(filename)
    if filename.endswith('.jpg'):
        img = cv2.imread(os.path.join(test_dir, filename))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        faces_rect = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

        for (x, y, w, h) in faces_rect:
            face_roi = gray[y:y+h, x:x+w]
            test_images.append(face_roi)
            test_labels.append(int(filename.split('_')[0]))

# Predict the labels for test images
predicted_labels = []
for test_image in test_images:
    label, confidence = recognizer.predict(test_image)
    predicted_labels.append(label)

# Calculate accuracy of the model
accuracy = np.mean(np.array(predicted_labels) == np.array(test_labels))
print('Accuracy on test set: {:.2f}%'.format(accuracy*100))
