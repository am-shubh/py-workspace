import pytesseract
import os
import cv2
from PIL import Image

image = cv2.imread('C:\\Users\\....') # Path of image file
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# to threshold the image
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

#to blur the image
# gray = cv2.medianBlur(gray, 3)

fileName = "tempfile.jpg"
cv2.imwrite(fileName, gray)

# getting text from files
text = pytesseract.image_to_string(Image.open(fileName))
os.remove(fileName)

print(text)

cv2.imshow("Image",image)
cv2.imshow("Gray", gray)

cv2.waitKey(0)