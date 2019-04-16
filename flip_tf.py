import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
import cv2
import numpy as np
import matplotlib.image as mpimg
#IMAGE_SIZE = 512
path = "C:\\Users\\....."
a=[]
#counter = 1

def flip_images(X_imgs):
    X_flip = []
    tf.reset_default_graph()
    X = tf.placeholder(tf.float32, shape = (None, None, 3))
    tf_img1 = tf.image.flip_left_right(X)
    #tf_img2 = tf.image.flip_up_down(X)
    #tf_img3 = tf.image.transpose_image(X)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())

        for index, file_path in enumerate(X_imgs):
            img = mpimg.imread(file_path)[:, :, :3] # Do not read alpha channel.
            flipped_imgs = sess.run(tf_img1, feed_dict = {X: img})
            X_flip.extend(flipped_imgs)
            img_to_save = cv2.cvtColor(flipped_imgs, cv2.COLOR_RGB2BGR)
            cv2.imwrite('..flip/'+file_path, img_to_save)
            
        '''for img in X_imgs:
            flipped_imgs = sess.run(tf_img1, feed_dict = {X: img})
            #cv2.imwrite('new/new'+str(counter), flipped_imgs)
            X_flip.extend(flipped_imgs)
            #counter = counter + 1
            '''
    X_flip = np.array(X_flip, dtype = np.float32)
    return X_flip
	

os.chdir(path)
a =os.listdir()

flipped_images = flip_images(a)
print(flipped_images.shape)
