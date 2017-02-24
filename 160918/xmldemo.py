#xml

#在 Python 中使用 SAX 解析 XML 非常简洁，通常我们关心的事件是
#start_element，end_element 和 char_data，准备好这 3 个函数，然后就可以解析 xml 了。

from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
	def start_element(self, name, attrs):
		print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
	def end_element(self, name):
		print('sax:end_element: %s' % name)
	def char_data(self, text):
		print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
 <li><a href="/python">Python</a></li>
 <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
res = parser.Parse(xml)
print(res)













