import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
	ret, frame = cap.read()
	rows, cols = frame.shape[:2]

    # generating vignette mask using Gaussian kernels
	kernel_x = cv2.getGaussianKernel(cols,200)
	kernel_y = cv2.getGaussianKernel(rows,200)
	kernel = kernel_y * kernel_x.T
	mask = 255 * kernel / np.linalg.norm(kernel)
	output = np.copy(frame)
	
	# applying the mask to each channel in the input image
	for i in range(3):
		output[:,:,i] = output[:,:,i] * mask

	cv2.imshow('Original', frame)
	cv2.imshow('Vignette', output)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()