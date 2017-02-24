#thread 
#Python 的线程是真正的 PosixThread，而不是模拟出来的线程。

#Python 的标准库提供了两个模块：_thread 和 threading，_thread 是低级
#模块，threading 是高级模块，对_thread 进行了封装。绝大多数情况下，
#我们只需要使用 threading 这个高级模块。

import time, threading

def loop():
	print('thread %s is running```' % threading.current_thread().name)
	n = 0
	while n<5:
		n+=1
		print('thread %s >>> %s' % (threading.current_thread().name,n))
		time.sleep(1)
	print('thread %s  ended' % (threading.current_thread().name))
print('thread %s is running```' % threading.current_thread().name)
t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread %s ended```' % threading.current_thread().name)


#look
import time, threading
balance = 0
def change_it(n):
	# 先存后取，结果应该为 0:
	global balance
	balence += n
	balence -= n

lock = threading.Lock()
def run_thread(n):
	for i in range(1000):
		# 先要获取锁:
		lock.acquire()
	try:
		# 放心地改吧:
		change_it(n)
	finally:
		# 改完了一定要释放锁:
		lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)




#死循环
#启动与 CPU 核心数量相同的 N 个python死循环线程，在 4 核 CPU 上可以监控到 CPU
#占用率仅有 102%，也就是仅使用了一核。

#但是用 C、C++或 Java 来改写相同的死循环，直接可以把全部核心跑满，
#4 核就跑到 400%，8 核就跑到 800%，为什么 Python 不行呢？

#因为 Python 的线程虽然是真正的线程，但解释器执行代码时，有一个GIL 锁
#这个 GIL 全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在 Python 中只能交替执行，即使 100 个线程跑在 100 核 CPU 上，也只能用到 1 个核。

#GIL 是 Python 解释器设计的历史遗留问题，通常我们用的解释器是官方
#实现的 CPython，要真正利用多核，除非重写一个不带 GIL 的解释器。

#所以，在 Python 中，可以使用多线程，但不要指望能有效利用多核。


#ThreadLocal 最常用的地方就是为每个线程绑定一个数据库连接，HTTP
#请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以
#非常方便地访问这些资源。








#进程 vs. 线程
#多进程模式最大的优点就是稳定性高，因为一个子进程崩溃了，不会影
#响主进程和其他子进程。（当然主进程挂了所有进程就全挂了，但是
#Master 进程只负责分配任务，挂掉的概率低）著名的 Apache 最早就是
#采用多进程模式。

#多线程模式通常比多进程快一点，但是也快不到哪去，而且，多线程模
#式致命的缺点就是任何一个线程挂掉都可能直接造成整个进程崩溃，因
#为所有线程共享进程的内存。在 Windows 上，如果一个线程执行的代
#码出了问题，你经常可以看到这样的提示：“该程序执行了非法操作，
#即将关闭”，其实往往是某个线程出了问题，但是操作系统会强制结束
#整个进程。



#计算密集型 vs. IO 密集型
#计算密集型  C
# IO 密集型 python






#异步 IO
#如果充分利用操作系统提供的异步 IO 支持，就可以用单进程单
#线程模型来执行多任务，这种全新的模型称为事件驱动模型，Nginx 就
#是支持异步 IO 的 Web 服务器，它在单核 CPU 上采用单进程模型就可
#以高效地支持多任务。







