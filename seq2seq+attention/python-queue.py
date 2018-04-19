#encoding=utf-8

import Queue
myqueue = Queue.Queue(maxsize=10)

#maxsize小于1就表示队列长度无限

myqueue.put(10)

myqueue.get()
# 调用队列对象的get()方法从队头删除并返回一个项目。

