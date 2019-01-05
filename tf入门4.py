import tensorflow as tf

#讲解placeholder

input1=tf.placeholder(tf.float32)
input2=tf.placeholder(tf.float32)
output=tf.multiply(input1,input2)

with tf.Session() as sess:
    print(sess.run(output,feed_dict={input1:[[7.0,3.0]],input2:[[6.0,2.0]]}))

