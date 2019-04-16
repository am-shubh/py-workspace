#from PIL import Image
import os
import random

path = "C:\\Users\\...."   #path of folder containing images
a = []
os.chdir(path)
a =os.listdir()
#random.shuffle(a)


for x in range(0,len(a),2):
    os.remove(a[x])
