# encoding=utf-8

import threading
import time

class myThread(threading.Thread):
	def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
    	print("starting" + self.name)
    	threadLock.acquire()
    	print_time(self.name,self.counter,3)
    	threadLock.release()

    def print_time(threadName, delay, counter):
     	while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time()))) 
        counter -= 1

threadLock = threading.lock()
threads = []


#创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

#等待所有线程新线程完成
for t in threads:
    t.join()
print("Exiting Main  Thread")