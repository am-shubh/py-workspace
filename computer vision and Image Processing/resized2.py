import cv2
import os

path = "C:\\Users\\...."   #path of folder containing images
a = []
os.chdir(path)
a =os.listdir()

height = 256
width = 256

for x in range(len(a)):
    image = cv2.imread(a[x])
    resized = cv2.resize(image, (height, width), interpolation = cv2.INTER_AREA)
    cv2.imwrite("C:\\Users\\....\\"+a[x], resized)
    
