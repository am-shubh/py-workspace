import cv2
import numpy as np

kernel_sharpen = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
# kernel_sharpen = np.array([[1,1,1], [1,-7,1], [1,1,1]])

cap = cv2.VideoCapture(0)

while(True):
	# getting each frame
    ret, frame = cap.read()

    outputFrame = cv2.filter2D(frame, -1, kernel_sharpen)

    cv2.imshow('Sharpened Image', outputFrame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
    	break

cap.release()
cv2.destroyAllWindows()