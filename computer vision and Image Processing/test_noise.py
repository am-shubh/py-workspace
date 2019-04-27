from scipy import misc
import numpy as np
import os
import cv2
path = "C:\\Users\\....\\"

os.chdir(path)

def add_noise():
    image  = misc.imread(path+'sample.jpg')
    noisy1 = image + image.std() * np.random.random(image.shape)
    misc.imsave('new100.jpg',noisy1)
    noisy4 = image + 0.75 * image.std() * np.random.random(image.shape)
    misc.imsave('new75.jpg',noisy4)
    noisy5 = image + 0.50 * image.std() * np.random.random(image.shape)
    misc.imsave('new50.jpg',noisy5)
    noisy6 = image + 0.25 * image.std() * np.random.random(image.shape)
    misc.imsave('new25.jpg',noisy6)
     
    
add_noise()
print('done')

