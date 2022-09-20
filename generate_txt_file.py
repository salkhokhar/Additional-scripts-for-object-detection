
'''
Some implementations of YOLO architecture need a txt file that lists
the path of each image that is to be used for training, validation or
testing.
This script generates that text file.
'''
import os

image_files = []
# my images files for training were located in the folder images/train
# this folder and the script were both present inside the main YOLO algorithm directory 
os.chdir(os.path.join("images", "train")) # change the "images" and "train" according to your folders' names
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        image_files.append("images/train/" + filename) # make the relevant changes here too
os.chdir("..")
with open(r"D:\yolov7\train.txt", "w") as outfile: # path of the txt file you want to create. Label it as train.txt, val.txt or test.txt accordingly.
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")
