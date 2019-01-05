import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
#讲解激活函数


def add_layer(inputs,in_size,out_size,activation_function=None):
    with tf.name_scope('layer'):
        with tf.name_scope('wights'):
            Weights=tf.Variable(tf.random_normal([in_size,out_size]))
        with tf.name_scope('biases'):
            biases=tf.Variable(tf.zeros([1,out_size])+0.0001)
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b=tf.matmul(inputs,Weights)+biases
        if activation_function is None:
            outputs=Wx_plus_b
        else:
            outputs=activation_function(Wx_plus_b)
        return  outputs



x_data=np.linspace(-1,1,300)[:,np.newaxis]
noise=np.random.normal(0,0.05,x_data.shape)
y_data=np.square(x_data)-0.5+noise


with tf.name_scope('inputs'):
    xs=tf.placeholder(tf.float32,[None,1],name='x_input')
    ys=tf.placeholder(tf.float32,[None,1],name='y_input')


l1=add_layer(xs,1,10,activation_function=tf.nn.relu)
l2=add_layer(l1,10,10,activation_function=tf.nn.relu)
predition=add_layer(l2,10,1,activation_function=None)

with tf.name_scope('loss'):
    loss=tf.reduce_mean(tf.reduce_sum(tf.square(ys-predition),reduction_indices=[1]),name='reduce_mean')

with tf.name_scope('train'):
    train_step=tf.train.RMSPropOptimizer(1e-3).minimize(loss)


init=tf.initialize_all_variables()


sess = tf.Session()
writer=tf.summary.FileWriter("D:\data\logs",sess.graph)
sess.run(init)
for i in range(10000):
    sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
    if i%1000==0:
        print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))
plt.scatter(x_data, y_data)
plt.scatter(x_data, sess.run(predition,feed_dict={xs:x_data,ys:y_data}))
plt.show()




