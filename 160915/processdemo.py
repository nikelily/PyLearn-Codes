#process进程

from multiprocessing import Process
import os

def run_proc(name):
	print('run child %s (%s)``'% (name,os.getpid))

if __name__=='__main__':
	print('parent process %s.'% os.getpid())
	p = Process(target = run_proc,args=('test',))
	print('child will be pro')
	p.start()
	p.join()
	print('child will be ended')
#创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process 实例，用 start()方法启动，这样创建进程比 fork()还要简单。
#join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。


print()
#pool进程池
from multiprocessing import Pool
import os,time,random

def long_time_task(name):
	print('run task %s (%s)````'%(name,os.getpid()))
	start = time.time()
	time.sleep(random.random() *5)
	end = time.time()
	print('task %s runs %0.2f sec.'%(name,(end-start)))

if __name__ == '__main__':
	print('parent process %s.'%os.getpid())
	p = Pool(4)
	for i in range(5):
		p.apply_async(long_time_task,args=(i,))
	print('waiting for all subproc done````')
	p.close()
	p.join()
	print('all subproc done')





#子进程,子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。

import subprocess
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup','www.python.org'])
print('exist code:',r)



#进程间通信
#Python 的 multiprocessing 模块包装了底层的机制，提供了Queue、Pipes 等多种方式来交换数据。

#以 Queue 为例，在父进程中创建两个子进程，一个往 Queue 里写数据，一个从 Queue 里读数据：
from multiprocessing import Process,Queue
import os,time,random

def write(q):# 写数据进程执行的代码
	print('process to write: %s' % os.getpid())
	for value in['a','b','c']:
		print('put %s to queue```'% value)
		q.put(value)
		time.sleep(random.random())

def read(q):# 读数据进程执行的代码
	print('process to read:%s'% os.getpid())
	while True:
		value = q.get(True)
		print('Get %s from queue.'% value)

if __name__ == '__main__':# 父进程创建 Queue，并传给各个子进程：
	q = Queue()
	pw = Process(target = write,args=(q,))
	pr = Process(target = read,args=(q,))

	pw.start()# 启动子进程 pw，写入:
	pr.start()# 启动子进程 pr，读取:
	pw.join()# 等待 pw 结束
	pr.terminate()# pr 进程里是死循环，无法等待其结束，只能强行终止







#小结
#在 Unix/Linux 下，可以使用 fork()调用实现多进程。
#要实现跨平台的多进程，可以使用 multiprocessing 模块。
#进程间通信是通过 Queue、Pipes 等实现的。











