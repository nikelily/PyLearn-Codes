#常用内建模块

#datetime
from datetime import datetime
now = datetime.now()
stampnow = now.timestamp() #注意 Python 的 timestamp 是一个浮点数。如果有小数位，小数位表示毫秒数。
print(now)
print(stampnow)
print(type(now))

dt = datetime(1994,3,7,12,23)
dtstamp = dt.timestamp()
print(dt)
#某些编程语言（如 Java 和 JavaScript）的 timestamp 使用整数表示毫秒
#数，这种情况下只需要把 timestamp 除以 1000 就得到 Python 的浮点表示方法。
dttime = datetime.fromtimestamp(dtstamp)
print(dttime)
#注意到 timestamp 是一个浮点数，它没有时区的概念，而 datetime 是有时区的。datetime做转换时已将时间转换为本地时区的时间

dttimeutc = datetime.utcfromtimestamp(dtstamp)
print(dttimeutc) # UTC 时间






#str 转换为 datetime
timestr = '2016-9-18 10:12:12'
timepattern = '%Y-%m-%d %H:%M:%S'
cday = datetime.strptime(timestr,timepattern)
print(cday)#注意转换后的 datetime 是没有时区信息的。


#datetime 转换为 str
now = datetime.now()
print(now.strftime(timepattern))
pattern2 = '%a, %b %d %H:%M'
print(now.strftime(pattern2))





from datetime import datetime, timedelta, timezone
tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区 UTC+8:00
now = datetime.now()
print(now)

