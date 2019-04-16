import cv2
import numpy as np
import os

# Playing video from file:
cap = cv2.VideoCapture('C:\\Users\\....')

try:
    if not os.path.exists('data/'):
        os.makedirs('data/')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 1
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == False:
        break
    num = str(currentFrame)
    num = num.zfill(4)
    # Saves image of the current frame in jpg file
    name = './data/' + num + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
