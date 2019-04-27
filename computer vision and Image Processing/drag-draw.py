import cv2
import numpy as np

ix,iy,fx,fy = -1,-1,-1,-1

# mouse callback function
def draw(event,x,y,flags,param):
    global ix,iy,fx,fy

    if event == cv2.EVENT_LBUTTONDOWN:
        ix,iy = x,y

    elif event == cv2.EVENT_LBUTTONUP:
        fx,fy = x,y
        cv2.rectangle(img,(ix,iy),(fx,fy),(0,255,0),1)


def crop():
    cropped = img[iy+1:fy-1, ix+1:fx-1]
    cv2.imshow("cropped", cropped)
    cv2.waitKey(0)


img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw)


while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    elif k==ord('c'):
        crop()


cv2.destroyAllWindows()
