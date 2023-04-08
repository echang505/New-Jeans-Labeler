import cv2
import numpy as np
import os

# Load the saved model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trained_data.yml')

# Set the video file path
video_path = 'Videos/OMG_Trim.mp4'

# Set the output video file path
output_path = 'VideoResult/OMG_Trim.mp4'

# Open the video file
cap = cv2.VideoCapture(video_path)

# Get the video frame rate
frame_rate = int(cap.get(cv2.CAP_PROP_FPS))

# Get the video frame size
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# Create a video writer object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, frame_rate, frame_size)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

frame_count = 0
# Process each frame
while True:
    # Read a frame from the video
    ret, frame = cap.read()
    frame_count += 1
    if not ret:
        break
    print("frame number: " + str(frame_count) + " / " + str(total_frames))
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces_rect = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    # Recognize faces in the frame and draw labels
    for (x, y, w, h) in faces_rect:
        face_roi = gray[y:y+h, x:x+w]
        label, confidence = recognizer.predict(face_roi)

        if label == 1:
            new_label = "dani"
        elif label == 2:
            new_label = "haerin"
        elif label == 3:
            new_label = "hanni"
        elif label == 4:
            new_label = "hyein"
        elif label == 5:
            new_label = "minji"

        cv2.putText(frame, new_label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Write the frame to the output video file
    out.write(frame)

# Release the video capture and writer objects
cap.release()
out.release()
