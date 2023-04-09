import cv2

# Open the video file
cap = cv2.VideoCapture('TrainingVideos/minji.mp4')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Initialize a counter for the frame number
frame_no = 0
fname = 'minji'
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Loop over the frames in the video stream
while True:
    # Read a frame from the video stream
    ret, frame = cap.read()

    # Check if the frame was read successfully
    if not ret:
        break

    # Increment the frame number
    frame_no += 1
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    eyes = eye_cascade.detectMultiScale(gray)
    print("frame number: " + str(frame_no) + " / " + str(total_frames))
    
    print (len(faces))
    print (len(eyes))


    if len(faces) != 1:
        continue
    
    if len(eyes) <= 1:
        continue


    # Construct the output file name by adding the frame number to the prefix
    output_file = 'TrainingVideosResult/' + fname + '/' + fname + '_{:04d}.jpg'.format(frame_no)

    # Write the frame as a JPEG image file
    cv2.imwrite(output_file, frame)

# Release the video stream
cap.release()


