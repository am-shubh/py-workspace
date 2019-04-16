import os
import argparse
import cv2
import numpy as np
from skimage.measure import structural_similarity as ssim

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True, help="name of folder")
args = vars(ap.parse_args())

path = "C:\\Users\\....\\{}".format(args["name"])   #path of folder containing images
a = []

os.chdir(path)
a =os.listdir()
x=0
while(x!=len(a)-1):
    current_img = cv2.imread(a[x])
    next_img = cv2.imread(a[x+1])
    gray_curr = cv2.cvtColor(current_img, cv2.COLOR_BGR2GRAY)
    gray_next = cv2.cvtColor(next_img, cv2.COLOR_BGR2GRAY)
    s = ssim(gray_curr, gray_next)
    print('difference between '+a[x]+' and '+a[x+1]+' is %.2f'%s)
    if(s>0.6):
        print('Deleting.. '+a[x+1])
        os.remove(a[x+1])
        a.pop(x+1)
        x=x-1
    x=x+1
