fd = open('test','a')


#　写操作
fd.write('hello　死鬼\n')
fd.write('干啥呀')

# 写入一个列表内容
# fd.writelines(['hello\n','world\n'])


fd.close()