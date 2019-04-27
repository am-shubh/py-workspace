import cv2
import os
import random
path = "Path of folder containing images"
a=[]
value = []
start = 20
end = 50

def increase_brightness(imgs, value):
    i = 1
    for img in imgs:
        img = cv2.imread(img)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        lim = 255 - value[i-1]
        v[v > lim] = 255
        v[v <= lim] += value[i-1]

        final_hsv = cv2.merge((h, s, v))
        img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
        cv2.imwrite('../brightened/new'+str(i)+'.jpg',img)	#saves image in new folder called brightened
        i += 1

os.chdir(path)
a =os.listdir()

for j in range(len(a)):
    value.append(random.randint(start, end))

increase_brightness(a,value)