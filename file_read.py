#　文件的读操作演示
import time

#　打开文件返回文件对象
fd = open('test','r')

# 　读操作
while True:
    #　每次读取８字节
    data = fd.read(8)
    #　如果读到空表示文件已经读完
    if not data:
        break
    print("读取到的内容：",data)

#　读取一行内容
# data = fd.readline()
# print("读取到的内容：",data)

#　将读取内容作为列表返回
# data = fd.readlines()
# print("读取到的内容：",data)

#　ｆｄ为可迭代对象，使用for循环每次获取一行内容
for line in fd:
    print("每行内容：", line)

# 关闭文件
fd.close()