from PIL import Image
import os

path = "C:\\Users\\...."   #path of folder containing images
a = []
os.chdir(path)
a =os.listdir()

height = 256
width = 256

for x in range(len(a)):
    tempImg = Image.open(a[x])
    newTempImg = tempImg.resize((int(width),int(height)))
    newTempImg.save(a[x])
    
