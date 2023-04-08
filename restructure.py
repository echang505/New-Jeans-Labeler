import os
import re
import shutil

folder_path = 'TestingImages'  # specify the path of the folder here
results_path = 'StructuredTestingImages'

# iterate over all the files in the folder
os.makedirs(results_path, exist_ok=True)

for foldername in os.listdir(folder_path):
    # check if the file is a JPEG image
    label = foldername.split('_')[0]
    print(foldername)
    print(label)

    for filename in os.listdir(folder_path + '/' + foldername):
        if filename.endswith('.jpg') or filename.endswith('.jpeg'):
            print(filename)
            number = re.findall('\d+', filename)[0]
            extension = os.path.splitext(filename)[1]
            new_filename = label + "_" + number + extension
            print(new_filename)
            shutil.copy(os.path.join(folder_path, foldername, filename), os.path.join(results_path, new_filename))


        # # rename the file
        #     new_filename = f"{label.zfill(3)}_{filename}"
        #     os.rename(os.path.join(folder_path, filename), os.path.join(results_path, new_filename))