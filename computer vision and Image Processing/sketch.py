import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    # getting each frame
    ret, frame = cap.read()

    imageGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    imageGray = cv2.medianBlur(imageGray, 7)

    edges = cv2.Laplacian(imageGray, cv2.CV_8U, ksize=5)
    ret, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)

    cv2.imshow("Sketch", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


