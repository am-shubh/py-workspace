import cv2
import numpy as np

size = 15
kernel_motion_blur = np.zeros((size, size))
kernel_motion_blur[int((size-1)/2), :] = np.ones(size)
kernel_motion_blur = kernel_motion_blur / size

cap = cv2.VideoCapture(0)

while(True):
	# getting each frame
    ret, frame = cap.read()

    outputFrame = cv2.filter2D(frame, -1, kernel_motion_blur)

    cv2.imshow('Motion Blur', outputFrame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
    	break

cap.release()
cv2.destroyAllWindows()