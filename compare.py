import os
from skimage.measure import structural_similarity as ssim
import numpy as np
import cv2

path = "C:\\Users\\....."   #path of folder containing images

a = []
os.chdir(path)
a =os.listdir()
prevImg = cv2.imread(a[0])

for x in range(len(a)):
    newImg = cv2.imread(a[x])
    s = ssim(prevImg, newImg)
    print(s)
    oldImg = newImg
