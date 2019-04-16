import cv2
import os

path = "C:\\Users\\Shubham\\Desktop\\test videos\\samples\\frames"
a = []
os.chdir(path)
a=os.listdir()
output = 'test_vid2.avi'

img = cv2.imread(a[0])
height, width, channels = img.shape

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output, fourcc, 10.0, (width,height))

for imgs in a:
    Img = cv2.imread(imgs)
    out.write(Img)

out.release()
cv2.destroyAllWindows()
