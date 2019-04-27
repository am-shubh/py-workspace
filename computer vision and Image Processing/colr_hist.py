# import the necessary packages
from matplotlib import pyplot as plt
import numpy as np
import cv2

image = cv2.imread('image.jpg')
image1 = cv2.imread('image1.jpg')
#cv2.imshow('image', image)

# grab the image channels, initialize the tuple of colors,
# the figure and the flattened feature vector
chans = cv2.split(image)
colors = ("b", "g", "r")
##plt.figure()
##plt.title("'Flattened' Color Histogram")
##plt.xlabel("Bins")
##plt.ylabel("# of Pixels")
features = []

# loop over the image channels
for (chan, color) in zip(chans, colors):
	# create a histogram for the current channel and
	# concatenate the resulting histograms for each
	# channel
	hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
	features.extend(hist)

	# plot the histogram
	#plt.plot(hist, color = color)
	#plt.xlim([0, 256])

#plt.show()

feat = []
chans = cv2.split(image1)
for (chan, color) in zip(chans, colors):
	# create a histogram for the current channel and
	# concatenate the resulting histograms for each
	# channel
	hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
	feat.extend(hist)

if(feat == features):
    print('yes..they are same')
else:
    print('nope..diff')

##cv2.waitKey(0)
##cv2.destroyAllWindows()
