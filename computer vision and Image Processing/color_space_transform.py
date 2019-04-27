import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
	# getting each frame
    ret, frame = cap.read()
    
    # Original image
    cv2.imshow('Original image', frame)

    # Convert to grayscale
    grayFrame = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale image', grayFrame)

    # Convert to YUV 
    yuvFrame = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2YUV)
    cv2.imshow('YUV image', yuvFrame)

    # Displaying the channels of YUV separately
    # cv2.imshow('Y channel', yuvFrame[:,:,0])
    # cv2.imshow('U channel', yuvFrame[:,:,1])
    # cv2.imshow('V channel', yuvFrame[:,:,2])

    # Convert to HSV
    hsvFrame = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2HSV)
    cv2.imshow('HSV image', hsvFrame)

    # Displaying the channels of HSV separately
    # cv2.imshow('H channel', hsvFrame[:,:,0])
    # cv2.imshow('S channel', hsvFrame[:,:,1])
    # cv2.imshow('V channel', hsvFrame[:,:,2])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()