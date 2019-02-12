#select 方法
# rs, ws, xs=select(rlist, wlist, xlist[,timout])
#rlist 传列表　想要关注的等待发生的IO事件
#wlist　列表　想要关注的可以主动处理的ＩＯ
#xlist 列表　想要关注的出现异常去处理的IO
# timeout 超时时间
from socket import *
import select
s = socket()
s.bind(('0.0.0.0',8888))
s.listen(3)
print("IO监控")
re,ws,xs=select.select([s],[],[])
print("就绪rs",rs)
print("就绪ws",ws)
print("就绪xs",xs)