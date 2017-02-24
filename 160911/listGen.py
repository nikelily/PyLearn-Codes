#列表生成式
L =  list(range(1, 11))
print(L)

P = []
for x in range(1,11):
	P.append(x*x)
print(P)
#等价于
print([x * x for x in range(1,11)])
#写列表生成式时，把要生成的元素 x * x 放到前面，后面跟 for 循环，就可以把 list 创建出来，十分有用

#for 循环后面还可以加上 if 判断
print([x * x for x in range(1,11) if x%2 == 0])

#还可以使用两层循环，可以生成全排列：
print([m + n for m in 'ABC' for n in 'XYZ'])


import os # 导入 os 模块，模块的概念后面讲到
print([d for d in os.listdir('.')])

