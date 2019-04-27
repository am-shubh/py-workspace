import cv2

book1 = cv2.imread('book1.jpg')
book2 = cv2.imread('book2.jpg')

difference = cv2.subtract(book1, book2)

cv2.imshow('difference-between-book',difference)
cv2.waitKey()
cv2.destroyAllWindows()

