#分布式进程
#在 Thread 和 Process 中，应当优选 Process，因为 Process 更稳定，而且，
#Process 可以分布到多台机器上，而 Thread 最多只能分布到同一台机器
#的多个 CPU 上。


#Python 的 multiprocessing 模块不但支持多进程，其中 managers 子模块还
#支持把多进程分布到多台机器上。



import random,time,queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()

class QueueManager(BaseManager):
	pass

QueueManager.register('get_task_queue',callable = lambda:task_queue)
QueueManager.register('get_result_queue',callable=lambda:result_queue)

manager = QueueManager(address=('',5000),authkey=b'abc')

manager.start()

task = manager.get_task_queue()
result = manager.get_result_queue()

for i in range(10):
	n = random.randint(0,10000)
	print('put task %d```'% n)
	task.put(n)

print('try get result')
for i in range(10):
	r = result.get(timeout = 10)
	print('result : %s'%r)

namager.shutdown()
print('master exit.')







