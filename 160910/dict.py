#dictionary
#哈希表实现,秒查询
#请务必注意，dict 内部存放的顺序和 key 放入的顺序是没有关系的

d = {'micheal':95,'scott':100}
print(d['scott'])

d['micheal'] = 59
print(d['micheal'])

d.pop('micheal')
print(d)

#和 list 比较，dict 有以下几个特点：
#1. 查找和插入的速度极快，不会随着 key 的增加而增加；
#2. 需要占用大量的内存，内存浪费多。
#而 list 相反：
#1. 查找和插入的时间随着元素的增加而增加；
#2. 占用空间小，浪费内存很少。


#正确使用 dict 非常重要，需要牢记的第一条就是 dict 的 key 必须是不可变对象。
#在 Python 中，字符串、整数等都是不可变的，因此，可以放心地作为 key。而 list 是可变的，就不能作为 key

