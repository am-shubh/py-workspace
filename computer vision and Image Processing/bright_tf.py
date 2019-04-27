import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
import cv2
import numpy as np
import matplotlib.image as mpimg
#IMAGE_SIZE = 512
path = "C:\\Users\\...."
a=[]
#counter = 1

def bright_images(X_imgs):
    X_flip = []
    tf.reset_default_graph()
    X = tf.placeholder(tf.float32, shape = (None, None, 3))
    tf_img1 = tf.image.adjust_brightness(X, delta = 0.3)
    #tf_img1 = tf.image.flip_left_right(X)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())

        for index, file_path in enumerate(X_imgs):
            img = mpimg.imread(file_path)[:, :, :] # Do not read alpha channel.
            brightened_images = sess.run(tf_img1, feed_dict = {X: img})
            X_flip.extend(brightened_images)
            #img_to_save = cv2.cvtColor(brightened_images, cv2.COLOR_RGB2BGR)
            cv2.imwrite('../bright/'+file_path, brightened_images)
            
    X_flip = np.array(X_flip, dtype = np.float32)
    return X_flip
	

os.chdir(path)
a =os.listdir()

brightened_images = bright_images(a)
print('done')
