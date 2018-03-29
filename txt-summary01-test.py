# coding=UTF-8


# 1、glob
# import glob

# # print(glob.glob(r"D:/github/reptile/*/*.jpg"))
# # print(glob.glob(r"./*.py"))

# f = glob.iglob(r'./*.py')
# print(f)

# for i in f:
# 	print(i)

#----------------------------------


# 2、random
# import random
# print(random.random())
# print(random.uniform(1,10)) # Random float x, 1.0 <= x < 10.0
# print(random.randint(1,10)) # Integer from 1 to 10, endpoints included
# print(random.randrange(0,101,2)) #  0-100间的偶数（even interger）
# print(random.choice('abcdefghij'))

# items = [1,2,3,4,5,6,7]
# random.shuffle(items)
# print(items)

# print(random.sample([1,2,3,4,5],3)) #选三个数

#-------------------------------------


# 3、struct
'''
数据格式为
姓名 年龄 性别   职业
lily 18  female teacher
'''

# import os
# import struct

# fp = open('test.bin','wb')

# name = b'lily'
# age = 18
# sex = b'female'
# job = b'teacher'

# fp.write(struct.pack('4si6s7s',name,age,sex,job))
# fp.flush()
# fp.close()

# fd = open('test.bin','rb')

# # 返回一个tuple
# print(struct.unpack('4si6s7s',fd.read())) #21个字节


#---------------------------------------

# 4、sys
import sys
print(sys.platform)
print(sys.path)