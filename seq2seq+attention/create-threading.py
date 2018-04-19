# 线程方法1：

import thread
import time

# 为线程定义一个函数
def print_time(threadName,delay):
	count = 0
	while count < 5:
		time.sleep(delay)
		count += 1
		print("%s:%s" % (threadName,time.ctime(time,time())))
	
try:
	thread.start_new_thread(print_time,("Thread-1",2,))
	thread.start_new_thread(print_time,("Thread-2",4,))
except:
	print("Error:unable to start thread")

while 1：
	pass

# Thread-1: Thu Jan 22 15:42:17 2009
# Thread-1: Thu Jan 22 15:42:19 2009
# Thread-2: Thu Jan 22 15:42:19 2009
# Thread-1: Thu Jan 22 15:42:21 2009
# Thread-2: Thu Jan 22 15:42:23 2009
# Thread-1: Thu Jan 22 15:42:23 2009
# Thread-1: Thu Jan 22 15:42:25 2009
# Thread-2: Thu Jan 22 15:42:27 2009
# Thread-2: Thu Jan 22 15:42:31 2009
# Thread-2: Thu Jan 22 15:42:35 2009


# 线程方法2：threading

import threading
import time

exitFlag = 0

class myThread(threading.Thread): #继承父类threading.Thread
	def __init__(self,threadID,name,counter):
		threading.Thread.__init__(self) # 只有self
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):
		print("starting" + self.name)
		print_time(self.name,self.counter,5)
		print("Exiting" + self.name)

	def print_time(threadName,delay,counter):
		while counter:
			if exitFlag:
				(threading.Thread).exit()
			time.sleep(delay)
			print("%s:%s" % threadName,time.ctime(time.time()))
			count -= 1

#创建新线程
thread1 = myThread(1,"Thread-1",1)
thread2 = myThread(2,"Thread-2",2)

#开启线程
thread1.start()
Thread2.start()