from scipy import misc
import numpy as np
import os
path = "C:\\Users\\...."
a=[]

def add_noise(imgs):
    for img in imgs:
        image  = misc.imread(img)
        noisy = image + image.std() * np.random.random(image.shape)
        misc.imsave('new'+img,noisy)


os.chdir(path)
a =os.listdir()

add_noise(a)
print('done')

