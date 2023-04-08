# New-Jeans-Labeler
- Labels each person in videos by their name using OpenCV

## /TRAININGIMAGES and /TESTINGIMAGES
  - Includes the dataset for training and testing the model
  - both should be structured like:
    #### [ID]_[NAME]/[NAME][IMAGENUM]
    - where [] is ignored and the inside is filled with the respective field. 
    - For example, 
    1_nwjnsdani is the folder name. dani1 is an image inside the folder.


## trainer.py
  - creates model using OpenCV face recognition
## restructure.py
  - restructures TestingImages to a format that can be tested by tester.py
  - Removes foldername and moves each image inside to RestructuredTestingImages with new name [ID]_[IMAGENUM]
## tester.py
  - tests model accuracy
## main.py
  - tests model on a video placed in /VIDEOS and result in /VIDEORESULT
