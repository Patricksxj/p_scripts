import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

X_data=np.random.rand(1000).astype(float)
Y_data=np.random.random_integers(1.0,100.0)*X_data**2+0.3232323



#定义变量
Weight=tf.Variable(tf.random_uniform([1],-1.0,1.0))
biases=tf.Variable(tf.zeros([1]))

y=Weight*(X_data**2)+biases

loss=tf.reduce_mean(tf.square(y-Y_data))

optimizer=tf.train.GradientDescentOptimizer(0.3)
train=optimizer.minimize(loss)

init=tf.initialize_all_variables()

sess=tf.Session()
sess.run(init)

for step in range(10000):
    sess.run(train)
    if step%200==0:
        print(step,sess.run(Weight),sess.run(biases))


plt.scatter(X_data,Y_data)

plt.scatter(X_data,sess.run(y))
plt.show()
