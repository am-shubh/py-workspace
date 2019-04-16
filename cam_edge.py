import numpy as np
import cv2

cap = cv2.VideoCapture(1)
 
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,200,255,cv2.THRESH_BINARY)
##    gray = cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY)
##    gray = cv2.GaussianBlur(gray, (7, 7), 0)
## 
##    edged = cv2.Canny(gray, 50, 100)
##    edged = cv2.dilate(edged, None, iterations=1)
##    edged = cv2.erode(edged, None, iterations=1)
    cv2.imshow('thresh',thresh)
    
##    image, contours, hierarchy = cv2.findContours(edged,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
##    cnt = cv2.drawContours(edged, contours, -1, (0,255,0), 3)
    
    #cv2.imshow('cnt',cnt)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
