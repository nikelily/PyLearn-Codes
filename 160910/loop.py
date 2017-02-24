#loop states
#Python 的循环有两种：

#一种是 for...in 循环，依次把 list 或 tuple 中的每个元素迭代出来:

names = ['scott','bob','tracy']
for name in names:
	print(name)

# range()函数，可以生成一个整数序列
sum = 0
for x in range(101):
	sum +=x
print(sum)

#第二种循环是 while 循环，只要条件满足，就不断循环，条件不满足时退出循环

sum = 0
n = 99
while n> 0:
	sum += n
	n -= 2
print(sum)