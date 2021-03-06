#-*- coding: UTF-8 -*-
import threading
import time
'''
#直接传入要运行的方法给线程以创建线程
def loop():
	print '%s is running' % threading.current_thread().name
	n = 0
	while n < 5:
		n += 1
		print 'thread %s >>>%d' %(threading.current_thread().name,n)
		time.sleep(1)
	print '%s end'%threading.current_thread().name

print '%s is running' %threading.currentThread().name

t = threading.Thread(target=loop,name = 'LoopThread-1')
t2 = threading.Thread(target=loop,name='LoopThread-2')
t.start()
t2.start()
t.join()  #此处作用相当于阻塞，也就是说后面的代码必须在t线程运行完了在运行而t2不受影响
          #（等待至t线程终止）

print '%s is end'%threading.current_thread().name

'''
'''
	所有线程间是并发运行的（包括主线程既该程序），所以当运行是会发现所有运行的过程都是交错的
不需要先运行完某段代码，再去运行后面的代码，而是前后文间交错运行
'''
#从Thread类继承，重写run方法

class myThread(threading.Thread):
	def __init__(self,threadID,name,counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter

	def run(self):
		print 'startting' + self.name
		threadLock.acquire()
		print_time(self.name,self.counter,5)
		threadLock.release()
		print 'exiting' + self.name

def print_time(threadName,delay,counter):
	while counter:
		time.sleep(delay)
		print "%s:%s" %(threadName,time.ctime(time.time()))
		counter -= 1
threadLock = threading.Lock()
thread1 = myThread(1,'thread-1',1)
thread2 = myThread(2,'thread-2',2)

thread1.start()
thread2.start()

print 'exit %s' %threading.currentThread().name








































































