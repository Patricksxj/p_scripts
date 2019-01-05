import tensorflow as tf

state=tf.Variable(0,name='counter')
#print(state)

one=tf.constant(1)
new_values=tf.add(state,one)
update=tf.assign(state,new_values)
init=tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))