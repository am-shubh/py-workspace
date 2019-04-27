# import the necessary packages

import numpy as np
import cv2

# load the image, convert it to grayscale, and blur it slightly
image = cv2.imread('book-after.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (7, 7), 0)

# perform edge detection, then perform a dilation + erosion to
# close gaps in between object edges
edged = cv2.Canny(gray, 50, 100)
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)

cv2.imshow('edges',edged)
cv2.waitKey(0)
cv2.destroyAllWindows()

