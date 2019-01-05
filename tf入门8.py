import os
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

print(os.getcwd())

os.chdir('D:/data')

print(os.getcwd())


# number 1 to 10 data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)


def add_layer(inputs,in_size,out_size,activation_function=None):
    with tf.name_scope('layer'):
        with tf.name_scope('wights'):
            Weights=tf.Variable(tf.random_normal([in_size,out_size]))
        with tf.name_scope('biases'):
            biases=tf.Variable(tf.zeros([1,out_size])+0.0001)
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b=tf.matmul(inputs,Weights)+biases
            #Wx_plus_b=tf.nn.dropout(Wx_plus_b,keep_prob)
        if activation_function is None:
            outputs=Wx_plus_b
        else:
            outputs=activation_function(Wx_plus_b)
        return  outputs


def compute_accuracy(v_xs,v_ys):
    global prediction
    y_pre=sess.run(prediction,feed_dict={xs:v_xs})
    correct_prediction=tf.equal(tf.argmax(y_pre,1),tf.argmax(v_ys,1))
    accuracy=tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
    result=sess.run(accuracy,feed_dict={xs:v_xs,ys:v_ys})
    return result

xs=tf.placeholder(tf.float32,[None,28*28])
ys=tf.placeholder(tf.float32,[None,10])
#keep_prob=tf.placeholder(tf.float32)

#add layer
l1=add_layer(xs,784,100,activation_function=tf.nn.sigmoid)
#l2=add_layer(l1,100,100,activation_function=tf.nn.relu)
prediction=add_layer(l1,100,10,activation_function=tf.nn.softmax)

#loss
#cross_entropy=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=ys,logits=prediction))
cross_entropy=tf.reduce_mean(-tf.reduce_sum(ys*tf.log(prediction),reduction_indices=[1]))
train_step=tf.train.GradientDescentOptimizer(0.6).minimize(cross_entropy)

sess=tf.Session()
sess.run(tf.initialize_all_variables())

for i in range(10000):
    batch_xs,batch_yx=mnist.train.next_batch(64)
    sess.run(train_step,feed_dict={xs:batch_xs,ys:batch_yx})
    if i %100==0:
        print(compute_accuracy(mnist.test.images,mnist.test.labels))




