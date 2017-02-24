#mail

#用 Outlook 或者 Foxmail 之类的软件写好邮件,
#电子邮件软件被称为 MUA：Mail User Agent——邮件用户代理

#Email 从 MUA 发出去，不是直接到达对方电脑，而是发到 MTA
#MTA：Mail Transfer Agent——邮件传输代理，就是那些 Email 服务提供商，比如网易、新浪等等

#Email 到达新浪的 MTA 后，由于对方使用的是@sina.com 的邮箱，因此，新浪的 MTA 会把 Email 投递到邮件的最终目的地 MDA
#MDA：Mail Delivery Agent——邮件投递代理
#Email 到达 MDA 后，就静静地躺在新浪的某个服务器上，存放在某个文件或特殊的数据库里，我们将这个长期保存邮件的地方称之为电子邮箱。

#Email 不会直接到达对方的电脑，因为对方电脑不一定开机，开机也不一定联网。对方要取到邮件，必须通过 MUA 从 MDA
#上把邮件取到自己的电脑上。


#所以，一封电子邮件的旅程就是：
#发件人 -> MUA -> MTA -> MTA -> 若干个 MTA -> MDA <- MUA <- 收件人

#``````````````````````````````````````````````````````````````````````````````````````````````````````````````

#要编写程序来发送和接收邮件，本质上就是：
#1. 编写 MUA 把邮件发到 MTA；
#2. 编写 MUA 从 MDA 上收邮件。

#``````````````````````````````````````````````````````````````````````````````````````````````````````````````

#发邮件时，MUA 和 MTA 使用的协议就是 SMTP：Simple Mail Transfer
#Protocol，后面的 MTA 到另一个 MTA 也是用 SMTP 协议。

#收邮件时，MUA 和 MDA 使用的协议有两种：
#POP：Post Office Protocol，目前版本是 3，俗称 POP3；
#IMAP：Internet Message Access Protocol，目前版本是 4，优点是不但能取邮件，还可以直接操作 MDA 上存储的邮件，比如从收件箱移到垃圾箱，等等。


#``````````````````````````````````````````````````````````````````````````````````````````````````````````````

#发送普通文字邮件

from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

# 输入 Email 地址和口令:
from_addr = input('From: ')
password = input('Password: ')
# 输入收件人地址:
to_addr = input('To: ')
# 输入 SMTP 服务器地址:
smtp_server = input('SMTP server: ')
import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP 协议默认端口是 25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()


#发送HTML邮件

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')
msg = MIMEText('<html><body><h1>Hello</h1>' +
	'<p>send by <a href="http://www.python.org">Python</a>...</p>' +
	'</body></html>', 'html', 'utf-8')

msg['From'] = _format_addr('Python 爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自 SMTP 的问候„„', 'utf-8').encode()
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()


#发送附件


#发送图片


#同时支持 HTML 和 Plain 格式






#加密 SMTP

#使用标准的 25 端口连接 SMTP 服务器时，使用的是明文传输，发送邮
#件的整个过程可能会被窃听。要更安全地发送邮件，可以加密 SMTP 会
#话，实际上就是先创建 SSL 安全连接，然后再使用 SMTP 协议发送邮件。






#使用 Python 的 smtplib 发送邮件十分简单，只要掌握了各种邮件类型的构造方法，正确设置好邮件头，就可以顺利发出。


#构造一个邮件对象就是一个 Messag 对象，如果构造一个 MIMEText 对象，
#就表示一个文本邮件对象，如果构造一个 MIMEImage 对象，就表示一个
#作为附件的图片，要把多个对象组合起来，就用 MIMEMultipart 对象，而
#MIMEBase 可以表示任何对象。它们的继承关系如下：
Message
+- MIMEBase
 +- MIMEMultipart
 +- MIMENonMultipart
 +- MIMEMessage
 +- MIMEText
 +- MIMEImage








