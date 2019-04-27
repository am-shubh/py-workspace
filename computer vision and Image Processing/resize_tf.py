import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
import cv2
import numpy as np
import matplotlib.image as mpimg
#cv2.imwrite('new'+i,resized_images)
IMAGE_SIZE = 512
path = "C:\\Users\\...."
a=[]

def tf_resize_images(X_img_file_paths):
    X_data = []
    tf.reset_default_graph()
    X = tf.placeholder(tf.float32, (None, None, 3))
    tf_img = tf.image.resize_images(X, (IMAGE_SIZE, IMAGE_SIZE), tf.image.ResizeMethod.NEAREST_NEIGHBOR)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        
        # Each image is resized individually as different image may be of different size.
        for index, file_path in enumerate(X_img_file_paths):
            img = mpimg.imread(file_path)[:, :, :3] # Do not read alpha channel.
            resized_img = sess.run(tf_img, feed_dict = {X: img})
            X_data.append(resized_img)
            #cv2.imwrite('new/new'+file_path, resized_img)

    X_data = np.array(X_data, dtype = np.float32) # Convert to numpy
    return X_data


os.chdir(path)
a =os.listdir()

dhinka = tf_resize_images(a)
print(dhinka.shape)

        
