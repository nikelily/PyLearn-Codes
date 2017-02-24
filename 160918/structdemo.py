#struct
#准确地讲，Python 没有专门处理字节的数据类型。但由于 str 既是字符串，又可以表示字节，所以，字节数组＝str。
#而在 C 语言中，我们可以很方便地用 struct、union 来处理字节，以及字节和 int，float 的转换

import struct
result = struct.pack('>I',10240099)#struct 的 pack 函数把任意数据类型变成 bytes：
#'>I'的意思是：>表示字节顺序是 big-endian，也就是网络序，I 表示 4 字节无符号整数。
print(result)

res2 = struct.unpack('>IH',b'\xf0\xf0\xf0\xf0\x80\x80')
print(res2)
#根据>IH 的说明，后面的 bytes 依次变为 I：4 字节无符号整数和 H：2字节无符号整数




#Windows 的位图文件（.bmp）是一种非常简单的文件格式，我们来用struct 分析一下:
#读入前 30 个字节来分析：

s =b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'

str = struct.unpack('<ccIIIIIIHH', s)
print(str)
#结果显示，b'B'、b'M'说明是 Windows 位图，位图大小为 640x360，颜色数为 24。





