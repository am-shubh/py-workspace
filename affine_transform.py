import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
	# getting each frame
    ret, frame = cap.read()
    rows, cols = frame.shape[:2]

    src_points = np.float32([ [0,0], [cols-1,0], [0, rows-1] ])
    dstn_points = np.float32([ [cols-1,0], [0,0], [cols-1,rows-1] ])

    affineMatrix = cv2.getAffineTransform(src_points, dstn_points)

    outputFrame = cv2.warpAffine(frame, affineMatrix, (cols,rows))
 
    cv2.imshow('frame',frame)
    cv2.imshow('Affine Transform', outputFrame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()