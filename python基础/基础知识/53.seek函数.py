#  seek()函数 用于移动文件指针

'''
文件对象.seek(偏移量，起始位置)

起始位置：
0：文件开头
1：当前位置
2：文件结尾
'''

f = open('test_52.txt', 'r+')

f.seek(3,0)

con = f.read()
print(con)

f.close()