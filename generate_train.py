import os

image_files = []
os.chdir(os.path.join("images", "train"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        image_files.append("images/train/" + filename)
os.chdir("..")
with open(r"D:\Python\PyTorch\yolov7\train.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")