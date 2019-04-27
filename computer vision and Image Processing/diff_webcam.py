import numpy as np
import cv2
import numpy as np

cap = cv2.VideoCapture(1)
ret, initial = cap.read()
cv2.imshow('initial',initial)
cv2.imwrite('without_book.jpg',initial)
cv2.waitKey()
cap.release()
sigma = 0.33

while(1):
    instruction = input("Enter C to capture again.")
    if(instruction == 'c'):
        cap = cv2.VideoCapture(1)
        ret, final = cap.read()
        cv2.imshow('final',final)
        cv2.imwrite('with_book.jpg',final)
        cv2.waitKey()
        cap.release()
        break

#print("Both image captured..calculating difference..")

difference = cv2.subtract(final, initial)
#cv2.imshow('difference',difference)
#cv2.imwrite('difference.jpg',difference)

gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (7, 7), 0)
cv2.imshow('gray',gray)
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
cv2.imshow('thresh',thresh)
cv2.imwrite('threshold.jpg',thresh)
v = np.median(thresh)
lower = int(max(0, (1.0 - sigma) * v))
upper = int(min(255, (1.0 + sigma) * v))
edged = cv2.Canny(thresh, lower, upper)

#edged = cv2.Canny(gray, 10, 20)
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)
cv2.imshow('edged',edged)
cv2.imwrite('edge.jpg',edged)
#ret,thresh = cv2.threshold(edged,127,255,0)
image, contours, hierarchy = cv2.findContours(edged,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

if len(contours) != 0:
    cnts = sorted(contours, key = cv2.contourArea, reverse = True)[:5]
    c = max(cnts, key = cv2.contourArea)
    x,y,w,h = cv2.boundingRect(c)
    # draw the book contour (in green)
    cv2.rectangle(final,(x,y),(x+w,y+h),(0,255,0),2)

##cnts = sorted(contours, key = cv2.contourArea, reverse = True)[:5]
##screenCnt = None
##for c in cnts:
##    # approximate the contour
##    peri = cv2.arcLength(c, True)
##    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
##
##    if len(approx) == 4:
##            screenCnt = approx
##            break
##
##cv2.drawContours(gray, [screenCnt], -1, (0, 255, 0), 3)
#img = cv2.drawContours(edged, contours, -1, (0,255,0), 3)
cv2.imshow('contours',final)
cv2.imwrite('final_contour.jpg',final)
cv2.waitKey()
cv2.destroyAllWindows()

    
 
