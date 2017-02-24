#advanced oop
#多重继承、定制类、元类

class Student(object):
	def __init__(self,name,score):
		self.name = name
		self.score = score
	
	def printl(self):
		print(self)

#尝试给实例绑定一个属性：
s = Student('scott',100)
s.pa = 'yeah'

#尝试给实例绑定一个方法：
def set_age(self,age):
	self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s)# 给实例绑定一个方法
s.set_age(89)
print(s.age)

# 给实例绑定一个方法
#为了给所有实例都绑定方法，可以给 class 绑定方法：
def set_score(self,score):
	self.score = score
Student.set_score = MethodType(set_score,Student)
#上面的 set_score 方法可以直接定义在 class 中，但动态绑
#定允许我们在程序运行的过程中动态给 class 加上功能，这在静态语言
#中很难实现。这就是动态语言的优势




#__slots__
#如果我们想要限制实例的属性怎么办？
#为了达到限制的目的，Python 允许在定义 class 的时候，定义一个特殊
#的__slots__变量，来限制该 class 实例能添加的属性：

class Student2(object):
	__slots__ = ('name','age') # 用 tuple 定义允许绑定的属性名称

s = Student2()
s.name = 'scott'
s.age = 12
#s.score = 99  #由于'score'没有被放到__slots__中，所以不能绑定 score 属性，

#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
#参数student就代表了传入父类，继承
class GraguateStudent(Student):
	pass




#使用@property
#在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但
#是，没办法检查参数，导致可以把成绩随便改：

#有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变
#量呢？对于追求完美的 Python 程序员来说，这是必须要做到的！

#Python 内置的@property 装饰器就是负责把一个方法变成属性调用的：
class Student3(object):

	@property
	def score(self):
		return self._score

	@score.setter
	def score(self,value):
		self._score = value


#@property 的实现比较复杂，我们先考察如何使用。把一个 getter 方法变成属性，只需要加上@property 就可以了，此时，@property 本身又创建了另一个装饰器@score.setter，负责把一个 setter 方法变成属性赋值，

s = Student3()
s.score = 90 # OK，实际转化为 s.set_score(60)
s.score # OK，实际转化为 s.get_score()





#多重继承

class Animal(object):
	pass

class Mammal (Animal):
	pass

class Bird(Animal):
	pass


#给动物再加上 Runnable 和 Flyable 的功能，只需要先定义好 Runnable 和 Flyable 的类
class Runnable(object):
	def run(self):
		print('Running````')

class Flyable(object):
	def fly(self):
		print('flying``````')


#对于需要 Runnable 功能的动物，就多继承一个 Runnable，例如 Dog：
class Dog(Mammal,Runnable):
	pass

class Bat(Mammal,Flyable):
	pass

class Parrot(Bird,Flyable):
	pass

class Ostrich(Bird,Runnable):
	pass


#MixIn：
#在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich
#继承自 Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现
#比如，让 Ostrich 除了继承自 Bird 外，再同时继承 Runnable。这种设计通常称之为 MixIn。

#MixIn 的目的就是给一个类增加多个功能，这样，在设计类的时候，我
#们优先考虑通过多重继承来组合多个 MixIn 的功能，而不是设计多层次
#的复杂的继承关系。

#Python自带的很多库也使用了MixIn。举个例子，Python自带了TCPServer
#和 UDPServer 这两类网络服务，而要同时服务多个用户就必须使用多进
#程或多线程模型，这两种模型由 ForkingMixIn 和 ThreadingMixIn 提供。
#通过组合，我们就可以创造出合适的服务来。

#class MyTCPServer(TCPServer,ForkingMixIn):
#	pass

#class MyUDPServer(UDPServer,ThreadingMaxIn):
#	pass

#由于 Python 允许使用多重继承，因此，MixIn 就是一种常见的设计。
#只允许单一继承的语言（如 Java）不能使用 MixIn 的设计。






#定制类

#__str__
class Student4(object):
	def __init__(self,name):
		self.name = name

print(Student4('scofield'))
#打印出一堆<__main__.Student object at 0x109afb190>，不好看

class Student4(object):
	def __init__(self,name):
		self.name = name
	def __str__(self):
		return 'Student4 object (name:%s)'%self.name

	__repr__ = __str__

print(Student4('wesley'))
#样打印出来的实例，不但好看，而且容易看出实例内部重要的数据。

#现直接敲变量不用 print，为直接显示变量调用的不是__str__()，而是__repr__()，两者的
#区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者
#看到的字符串，也就是说，__repr__()是为调试服务的。



#__iter__
#一个类想被用于 for ... in 循环，类似 list 或 tuple 那样，就必须实现一个__iter__()方法，
#Python 的 for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到 StopIteration 错误时退出循环。

class Fib(object):
	def __init__(self):
		self.a,self.b = 0, 1

	def __iter__(self):
		return self # 实例本身就是迭代对象，故返回自己

	def __next__(self):
		self.a,self.b = self.b,self.a+self.b # 计算下一个值
		if self.a>100000:#get over
			raise StopIteration()
		return self.a #return the next one

for n in Fib():
	print(n)



#__getitem__
#Fib 实例虽然能作用于 for 循环，看起来和 list 有点像，但是，把它当成
#list 来使用还是不行，比如，取第 5 个元素：
#要表现得像 list 那样按照下标取出元素，需要实现__getitem__()方法：

class Fib(object):
	def __init__(self):
		self.a,self.b = 0, 1

	def __iter__(self):
		return self # 实例本身就是迭代对象，故返回自己

	def __next__(self):
		self.a,self.b = self.b,self.a+self.b # 计算下一个值
		if self.a>100000:#get over
			raise StopIteration()
		return self.a #return the next one

	def __getitem__(self,n):
		a,b= 1,1
		for x in range(n):
			a,b = b,a+b
		return a

f = Fib()
print(f[0])
print(f[6])

#总之，通过上面的方法，我们自己定义的类表现得和 Python 自带的 list、
#tuple、dict 没什么区别，这完全归功于动态语言的“鸭子类型”，不需要
#强制继承某个接口。


#__getattr__
#正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。
#错误信息很清楚地告诉我们，没有找到 score 这个 attribute。
#要避免这个错误，除了可以加上一个 score 属性外，Python 还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。

class Student6(object):
	def __init__(self):
		self.name = 'scofield'

	def __getattr__(self,attr):
		if attr == 'score' :
			return 100
#当调用不存在的属性时，比如 score，Python 解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score 的值：
s = Student6();
print(s.score)
#返回函数也是完全可以的：
class Student6(object):
	def __init__(self):
		self.name = 'scofield'
	def __getattr__(self,attr):
		if attr=='age':
			return lambda :25
s = Student6();
print(s.age())
#注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如 name，不会在__getattr__中查找。





#__call__
#任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：

class Student9(object):
	def __init__(self,name):
		self.name = name
	def __call__(self):
		print('my name is %s.' % self.name)

s = Student9('scofield')
s()





