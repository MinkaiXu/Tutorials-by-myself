import tensorflow as tf

state = tf.Variable(0, name='counter')
new_value = tf.add(state, 1)
update = tf.assign(state, new_value)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for _ in range(5):
        sess.run(update)
        print([sess.run(state),sess.run(update)])
