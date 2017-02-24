#database


#为了便于程序保存和读取数据，而且，能直接通过条件快速查询到指定
#的数据，就出现了数据库（Database）这种专门用于集中存储和查询的软件。








#使用 SQLite
#。SQLite 的特点是轻量级、可嵌入，但不能承受高并发访问，适合桌面和移动应用。

#Python 定义了一套操作数据库的 API 接口，任何数据库要连接到Python，只需要提供符合 Python 标准的数据库驱动即可。
#由于 SQLite 的驱动内置在 Python 标准库中，所以我们可以直接来操作SQLite 数据库。
import sqlite3
conn = sqlite3.connect('test.db')
#连接到数据库后，需要打开游标，称之为 Cursor，通过 Cursor 执行 SQL语句，然后，获得执行结果。
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')

print( cursor.rowcount)
cursor.close()
conn.commit()
conn.close()







#在 Python 中操作数据库时，要先导入数据库对应的驱动，然后，通过Connection 对象和 Cursor 对象操作数据。






#使用 MySQL
#而 MySQL是为服务器端设计的数据库，能承受高并发访问，同时占用的内存也远远大于 SQLite。

#安装 MySQL 驱动:
#由于 MySQL 服务器以独立的进程运行，并通过网络对外服务，所以，
#需要支持 Python 的 MySQL 驱动来连接到 MySQL 服务器。MySQL 官
#方提供了 mysql-connector-python 驱动







#使用 SQLAlchemy

#可以用一个 list 表示多行，list 的每一个元素是tuple，表示一行记录，比如，包含 id 和 name 的 user 表：
#[
# ('1', 'Michael'),
# ('2', 'Bob'),
# ('3', 'Adam')
#]

#如果把一个 tuple 用 class 实例来表示，就可以更容易地看出表的结构来：

class User(object):
	def __init__(self, id, name):
	self.id = id
	self.name = name


#[
# User('1', 'Michael'),
# User('2', 'Bob'),
# User('3', 'Adam')
#]


#这就是传说中的 ORM 技术：Object-Relational Mapping，把关系数据库的表结构映射到对象上
#但是由谁来做这个转换呢？所以 ORM 框架应运而生。
#在 Python 中，最有名的 ORM 框架是 SQLAlchemy。













