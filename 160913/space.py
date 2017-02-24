#module & package

' a test module '#一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
__author__ = 'scott' #使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名

import sys #使用 sys 模块的第一步，就是导入该模块：

def test():
	args = sys.argv
	if len(args) == 1:
		print('hey')
	elif len(args) == 2:
		print('hey,%s!' % args[1])
	else:
		print('too many arguments')
	

if __name__ == '__main__' :
	test()


#在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用

#正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI 等
#类似_xxx 和__xxx 这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc 等

#print(sys.path)
