import cv2
import numpy as np

kernel_emboss_1 = np.array([[0,-1,-1],
                            [1,0,-1],
                            [1,1,0]])

kernel_emboss_2 = np.array([[-1,-1,0],
                            [-1,0,1],
                            [0,1,1]])

kernel_emboss_3 = np.array([[1,0,0],
                            [0,0,0],
                            [0,0,-1]])

cap = cv2.VideoCapture(0)

while(True):
	# getting each frame
    ret, frame = cap.read()
    grayImage = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    output_1 = cv2.filter2D(grayImage, -1, kernel_emboss_1)
    output_2 = cv2.filter2D(grayImage, -1, kernel_emboss_2)
    output_3 = cv2.filter2D(grayImage, -1, kernel_emboss_3)

    outputFrame = cv2.add(output_1, output_2, output_3)

    cv2.imshow('Input', frame) 
    cv2.imshow('Embossing', outputFrame + 128)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()