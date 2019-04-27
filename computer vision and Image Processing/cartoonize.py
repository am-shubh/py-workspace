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

    smallImg = cv2.resize(frame, None, fx=1.0/4, fy=1.0/4, interpolation=cv2.INTER_AREA)

    num_repetitions = 10
    sigma_color = 5
    sigma_space = 7
    size = 5

    for i in range(num_repetitions):
        smallImg = cv2.bilateralFilter(smallImg, size, sigma_color, sigma_space)

    temp = cv2.resize(smallImg, None, fx=4, fy=4, interpolation=cv2.INTER_LINEAR)

    outputFrame = np.zeros(imageGray.shape)
    outputFrame = cv2.bitwise_and(temp, temp, mask=mask)

    cv2.imshow("Cartoonize", outputFrame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


