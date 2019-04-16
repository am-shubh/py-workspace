import os
os.environ["CUDA_VISIBLE_DEVICES"]="1"
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf

x = tf.constant(5)
y = tf.constant(8)

result = tf.multiply(x,y)

with tf.Session() as sess:
    print(sess.run(result))
