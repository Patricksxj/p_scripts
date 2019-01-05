import tensorflow as tf
import numpy as np

a=tf.constant([[1.0,2.3]])
b=tf.constant([[1.0],[1.0]])
result=tf.matmul(a,b)

sess=tf.Session()
result2=sess.run(result)
print('result_tf1',result2)


with tf.Session() as sess:
    result2 = sess.run(result)
    print('result_tf2', result2)

sess.close()

#等价于如下方法
a_np=np.array([[1.0,2.3]])
b_np=np.array([[1.0],[1.0]])
result_np=np.dot(a_np,b_np)
print('result_np',result_np)