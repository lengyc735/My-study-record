from sys import argv
from os.path import exists    # exists判断文件是否存在

scropt, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))

# we could do these two on one line too, how?
input_file = open(from_file)    # 原来的变量是input，这里改为input_file，input是一个函数不可做变量名
indata = input_file.read()      # 读取文件内容，将from_file的内容赋值给indata

print("The input file is %d bytes long" % len(indata))  # 显示输入对象字节长度
 
print("Does the output file exist? %r" % exists(to_file))   # 这行作用是显示输出文件是否存在
print("Ready, hit RETURN to continue, CTRL-C to abort.")    # 提示用户按回车键继续，按CTRL-C中止操作                                                
input()   # 这里的input()是用来暂停程序的，作用是让用户有机会在复制文件之前中止操作

output = open(to_file, 'w')
output.write(indata)

print("Alright, all done.")  # 提示用户文件拷贝完成

output.close()
input_file.close()

# 这个脚本可以将一个文件的内容复制到另一个文件中