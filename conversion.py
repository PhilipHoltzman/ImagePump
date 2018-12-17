# basic script to convert png to jpeg
from PIL import Image
import os, sys, shutil

path2png = "/Users/poisonarena/Desktop/png"
path2jpg = "/Users/poisonarena/Desktop/jpg"

imageName = "image"
imageNum = 1

# file nav
print("running to the png directory")
os.chdir(path2png)
print(os.getcwd())

directory = os.fsencode(path2png)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".png"): 

        print("opening the file")
        targetImage = Image.open(file)
        print("converting... ")
        rgb_im = targetImage.convert('RGB')
        print("running to jpg folder")
        os.chdir(path2jpg)
        print("saving file.. ")
        rgb_im.save(imageName + str(imageNum) +'.jpg')
        imageNum = imageNum + 1

        print("deleting original... ")
        os.chdir(path2png)
        os.remove(file)

    else:
        print("something happened")
        continue


