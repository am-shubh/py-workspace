import cv2
import os
path = "Path of folder containig images"
a=[]

def contrast(imgs):
    i=1
    for img in imgs:
        img = cv2.imread(img)
        lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(8,8))
        l2 = clahe.apply(l)
        lab = cv2.merge((l2,a,b))
        img2 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
        cv2.imwrite('../contrast/new'+str(i)+'.jpg',img2)
        i += 1

os.chdir(path)
a =os.listdir()
random.shuffle(a)
contrast(a)
