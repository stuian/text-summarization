import os
import numpy as np 
import tensorflow as tf 
import cv2

def tolist(value):
	if type(value) == list:
		return value
	else:
		return [value]

def _int64_feature(value):
	value = tolist(value)
	value = [int(x) for x in value]
	return tf.train.Feature(int64_list = tf.train.Int64list(value = value))

def _float_feature(value):
	value = tolist(value)
	value = [float(x) for x in value]
    return tf.train.Feature(float_list=tf.train.FloatList(value = value))

def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value = toList(value)))

# make tfrecords
def MakeTFRecord(filename,tfrecords,imageroot):
	 # 创建一个TFRecordWriter来进行写入数据
	writer = tf.python_io.TFRecordWriter(tfrecords)
	fp = open(filename,'r')
	lines = fp.readlines()
	for line in lines:
		line = line.strip().split()
		imagepath = os.path.join(imageroot,line[0])
		print(imagepath)

		img = cv2.imread(imagePath,0)
		img = cv2.resize(img,(128,128))
		img_raw = img.tostring()

		example = tf.train.Example(
			features=tf.train.Features(
				feature={
                    "img_raw":_bytes_feature(img_raw),
                    "label": _int64_feature(line[1:])
                }
			))
		writer.write(example.SerializeToString())
	writer.close()

	Serialized_ex_it = tf.python_io.tf_record_iterator(tfrecords)
	for Serialized_ex in Serialized_ex_it:
		example = tf.train.Example()
		example.ParseFromString(serialized_ex)
		print(example)

		# 取出正确的key并且正确的类型的value值,错一个都会取不出值
	    image = example.features.feature['img_raw'].bytes_list.value
	    label = example.features.feature['label'].int64_list.value

	    print(image,label)


def ReadTFRecord(tfrecords):
    # 可以把多个tfrecords排成一个queue,这样可以方便的使用多个tfrecords文件
    record_queue = tf.train.string_input_producer([tfrecords])
    # 读取TFRecords器
    reader = tf.TFRecordReader()
    # 一个数据一个数据的读返回key-value值,都保存在serialized_ex中
    # 注意: 这里面keys是序列化的副产物,命名为tfrecords+random(),表示唯一的ID,没有作用,可以设置为_
    #keys, serialized_ex = reader.read(record_queue)
    _, serialized_ex = reader.read(record_queue)
    # 直接解析出features数据,并且使用固定特征长度,及每个Example中一定会存在一个image和一个label
    # 并不是输入的图片大小不同就使用VarLenFeature.
    features = tf.parse_single_example(serialized_ex,
            features={
                # 取出key为img_raw和label的数据,尤其是int位数一定不能错!!!
                'img_raw': tf.FixedLenFeature([],tf.string),
                'label': tf.FixedLenFeature([], tf.int64)
            })
    img = tf.decode_raw(features['img_raw'], tf.uint8)

    # 注意定义的为int多少位就转换成多少位,否则容易出错!!
    label = tf.cast(features['label'], tf.int64)
    return img, label

imgs,labels = ReadTFRecord(tfrecords)
sess = tf.Session()
# 多线程调节器
coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(sess=sess,coord=coord)
# 输出10个样本
for i in range(10):
    image,label = sess.run([imgs,labels])
    print image.shape,'label:', label
