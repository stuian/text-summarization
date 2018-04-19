# encoding=utf-8

import tensorflow as tf
import os

keys = [[1.0],[],[2.0,3.0]]
sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())

def make_example(key):
    example = tf.train.Example(features = tf.train.Features(
        feature={
            'ft':tf.train.Feature(float_list = tf.train.FloatList(value = key))
        }
    ))
    return example

filename = "tmp.tfrecords"
if os.path.exists(filename):
    os.remove(filename)
writer = tf.python_io.TFRecordWriter(filename)
for key in keys:
    ex = make_example(key)
    writer.write(ex.SerializeToString())
writer.close()

reader = tf.TFRecordReader()
filename_queue = tf.train.string_input_producer(["tmp.tfrecords"],num_epochs=1)
_,serialized_example = reader.read(filename_queue)

batch = tf.train.batch(tensors = [serialized_example],batch_size = 3)

features = {
    "ft":tf.VarLenFeature(tf.float32)
}

key_parsed = tf.parse_example(batch,features)

print(tf.contrib.learn.run_n(key_parsed))

# features = {
#     "ft":tf.FixedLenFeature(shape=[2],dtype=tf.float32)
# }
#
# key_parsed = tf.parse_example(batch,features)
# print(tf.contrib.learn.run_n(key_parsed))


#coding=utf-8

import tensorflow as tf
import os

sess=tf.InteractiveSession()
sess.run(tf.global_variables_initializer())

def make_example(key):
    example = tf.train.Example(features=tf.train.Features(
        feature={
            'ft':tf.train.Feature(float_list=tf.train.FloatList(value=key))
        }
    ))
    return example

features={
    "ft":tf.FixedLenFeature(shape=[3],dtype=tf.float32)
}

key_parsed = tf.parse_single_example(make_example([1.0,2.0,3.0]).SerializeToString(),features)

print tf.contrib.learn.run_n(key_parsed)

