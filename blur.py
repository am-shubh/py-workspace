import os
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True, help="name of folder")
args = vars(ap.parse_args())

path = "C:\\Users\\....\\{}".format(args["name"])  #path of folder containing images
a = []

os.chdir(path)
a =os.listdir()

for x in range(len(a)):
	
    img = cv2.imread(a[x])
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    check = cv2.Laplacian(gray, cv2.CV_64F).var()

    if(check < 160.0):
        os.remove(a[x])
    
