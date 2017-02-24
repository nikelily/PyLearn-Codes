#itertools

#Python 的内建模块 itertools 提供了非常有用的用于操作迭代对象的函数。
import itertools
natuals = itertools.count(1)#count()会创建一个无限的迭代器
#for n in natuals:
#	print(n)



#cycle()会把传入的一个序列无限重复下去：
cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
#for c in cs:
#	print(c)


#repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
ns = itertools.repeat('A',10)
for n in ns:
	print(n)




#无限序列只有在 for 迭代时才会无限地迭代下去，如果只是创建了一个
#迭代对象，它不会事先把无限个元素生成出来，事实上也不可能在内存
#中创建无限多个元素。


#无限序列虽然可以无限迭代下去，但是通常我们会通过 takewhile()等函
#数根据条件判断来截取出一个有限的序列：
natural = itertools.count(1)
ns = itertools.takewhile(lambda x:x<=10,natural)
print(list(ns))



#itertools 提供的几个迭代器操作函数更加有用：
#chain()
#groupby()
#
#
#




