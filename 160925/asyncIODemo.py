#异步 IO

#要解决的问题是 CPU 高速执行能力和 IO 设备的龟速严重不匹配
#1.多线程和多进程只是解决这一问题的一种方法
#2.另一种解决 IO 问题的方法是异步 IO

#异步 IO 模型需要一个消息循环，在消息循环中，主线程不断地重复“读取消息-处理消息”这一过程：

#loop = get_event_loop()
#while True:
#	event = loop.get_event()
#	process_event(event)


#在学习异步 IO 模型前，我们先来了解协程
#协程，又称微线程，纤程。英文名 Coroutine。

#协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转
#而执行别的子程序，在适当的时候再返回来接着执行。
#看起来 A、B 的执行有点像多线程，但协程的特点在于是一个线程执行


#Python 对协程的支持是通过 generator 实现的。




#asyncio 是 Python 3.4 版本引入的标准库，直接内置了对异步 IO 的支持。

import asyncio,threading

@asyncio.coroutine
def hello():
	print("Hello world! (%s)" % threading.currentThread())
	# 异步调用 asyncio.sleep(1):
	r = yield from asyncio.sleep(1)
	print("Hello again! (%s)" % threading.currentThread())



# 获取 EventLoop:
loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# 执行 coroutine
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

#@asyncio.coroutine 把一个 generator 标记为 coroutine 类型，然后，我们
#就把这个 coroutine 扔到 EventLoop 中执行。

#由打印的当前线程名称可以看出，两个 coroutine 是由同一个线程并发执行的。
#如果把 asyncio.sleep()换成真正的 IO 操作，则多个 coroutine 就可以由一个线程并发执行。







#asyncio 提供了完善的异步 IO 支持；
#异步操作需要在 coroutine 中通过 yield from 完成；
#多个 coroutine 可以封装成一组 Task 然后并发执行。




