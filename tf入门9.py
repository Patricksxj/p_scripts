import os
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import pandas as pd
#convolutional neural networks



print(os.getcwd())

os.chdir('D:/data')

print(os.getcwd())


# number 1 to 10 data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)



def compute_accuracy(v_xs,v_ys):
    global prediction
    y_pre=sess.run(prediction,feed_dict={xs:v_xs, keep_prob: 1})
    correct_prediction=tf.equal(tf.argmax(y_pre,1),tf.argmax(v_ys,1))
    accuracy=tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
    result=sess.run(accuracy,feed_dict={xs:v_xs,ys:v_ys,keep_prob: 1})
    return result


# 确认weight 与 biases
def weight_variable(shape):
    initial=tf.truncated_normal(shape,stddev=0.1)
    return tf.Variable(initial)


def bias_variable(shape):
    initial=tf.constant(0.01,shape=shape)
    return tf.Variable(initial)

#定义卷积层
def conv2d(x,W):
    return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME')

#定义池化层
def max_pool_2x2(x):
    return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')




xs=tf.placeholder(tf.float32,[None,784])
ys=tf.placeholder(tf.float32,[None,10])
keep_prob=tf.placeholder(tf.float32)

x_image=tf.reshape(xs,[-1,28,28,1])
#print(x_image.shape) # [n_sample,28,28]

## conv1 layer1 ##
W_conv1=weight_variable([5,5,1,32])#patch5*5 ,in sieze=1,outsieze=32
b_conv1=bias_variable([32])
h_conv1=tf.nn.relu(conv2d(x_image,W_conv1)+b_conv1) #output size 28*28*32
h_pool1=max_pool_2x2(h_conv1)   #output size 14*14*32


## conv2 layer2 ##
W_conv2=weight_variable([5,5,32,64]) #patch5*5 ,in size=32,outsieze=64
b_conv2=bias_variable([64])
h_conv2=tf.nn.relu(conv2d(h_pool1,W_conv2)+b_conv2) #output size 14*14*64
h_pool2=max_pool_2x2(h_conv2)   #output size 7*7*64


## func1 layer ##

W_f1=weight_variable([7*7*64,512])  #input size 7*7*64
b_fc1=bias_variable([512])
#[n_sample,7,7,64] ->> [n_sample,7*7*64]
h_pool2_flat=tf.reshape(h_pool2,[-1,7*7*64])
h_fc1=tf.nn.relu(tf.matmul(h_pool2_flat,W_f1)+b_fc1)
h_fc1_drop=tf.nn.dropout(h_fc1,keep_prob)


## func2 layer ##
W_f2=weight_variable([512,10])  #input size 7*7*64
b_fc2=bias_variable([10])
prediction=tf.nn.softmax(tf.matmul(h_fc1_drop,W_f2)+b_fc2)




#loss
#cross_entropy=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=ys,logits=prediction))
cross_entropy=tf.reduce_mean(-tf.reduce_sum(ys*tf.log(prediction),reduction_indices=[1]))
train_step=tf.train.AdamOptimizer(0.8e-3).minimize(cross_entropy)

sess=tf.Session()
sess.run(tf.initialize_all_variables())

result={}
for i in range(20000):
    batch_xs,batch_yx=mnist.train.next_batch(500)
    if i %100==0:
        sess.run(train_step,feed_dict={xs:batch_xs,ys:batch_yx, keep_prob:0.5})
    if i %100==0:
        testSet = mnist.test.next_batch(1000)
        result[i].append(compute_accuracy(testSet[0],testSet[1]))

sess.close()


output = pd.DataFrame(result,index=[0])
output.to_csv( "D:/P_WORKPLACE/tf_cnn_output.csv",index=False)