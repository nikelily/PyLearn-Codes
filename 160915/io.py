# -*- coding: utf-8 -*-
#IO

#读写文件是最常见的 IO 操作,用法和C 是兼容的。

f=open('F:\\python_workspace\\160915\\datas','r')
content = f.read()
print(content)
#文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的：
f.close 



#由于文件读写时都有可能产生 IOError，一旦出错，后面的 f.close()就不会调用
try:
	f = open('F:\\python_workspace\\160915\\datas','r')
	print(f.read())
finally:
	if f:
		f.close()

#，Python 引入了 with 语句来自动帮我们调用 close()方法：
#这和前面的 try ... finally 是一样的，但是代码更佳简洁
with open('F:\\python_workspace\\160915\\datas','r') as f:
	print(f.read())



#read(size),readline()
#如果文件很小，read()一次性读取最方便；
#如果不能确定文件大小，反复调用 read(size)比较保险；
#如果是配置文件，调用 readlines()最方便：
f = open('F:\\python_workspace\\160915\\datas','r')
for line in f.readlines():
	print(line.strip())# 把末尾的'\n'删掉
f.close()

#file-like Object
#像 open()函数返回的这种有个 read()方法的对象，在 Python 中统称为
#file-like Object。除了 file 外，还可以是内存的字节流，网络流，自定义
#流等等。

#二进制文件
#要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
f = open('C:\\Users\\scott\\Pictures\\1.jpg','rb')
print(f.read())
f.close()


#字符编码
#要读取非UTF-8编码的文本文件，需要给open()函数传入 encoding参数，
#例如，读取 GBK 编码的文件：
f = open('F:\\python_workspace\\160915\\datasInGBK', encoding='gbk')
print(f.read())
f.close()


#写文件和读文件是一样的，唯一区别是调用 open()函数时，传入标识符
#'w'或者'wb'表示写文本文件或写二进制文件：
f = open('F:\\python_workspace\\160915\\datas','w')
f.write('this file has bean altered')
f.close()
#你可以反复调用 write()来写入文件，但是务必要调用 f.close()来关闭文件。当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是
#放到内存缓存起来，空闲的时候再慢慢写入。只有调用 close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。忘记调用 close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了

#所以，还是用 with语句来得保险：
with open('F:\\python_workspace\\160915\\datas','w',encoding='gbk') as f:
	f.write('呵呵哒O(∩_∩)O哈哈~')




