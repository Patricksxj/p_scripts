import tensorflow as tf

#讲解placeholder

input1=tf.placeholder(tf.float32)
input2=tf.placeholder(tf.float32)
output=tf.multiply(input1,input2)

with tf.Session() as sess:
    print(sess.run(output,feed_dict={input1:[[7.0,3.0]],input2:[[6.0,2.0]]}))



x=tf.constant([[7.0,3.0]])

y=tf.constant([[6.0],[2.0]])

#x=tf.constant([[1.0,2.0,3.0],[1.0,2.0,3.0],[1.0,2.0,3.0]])
#y=tf.constant([[0,0,1.0],[0,0,1.0],[0,0,1.0]])


result=tf.matmul(x,y)

with tf.Session() as sess:
    print(sess.run(result))