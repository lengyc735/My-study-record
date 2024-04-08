import os

# 构造条件的数据
flag = 1

# 1. 找到所有文件： 获取当前目录下的所有文件
file_list = os.listdir()
print(file_list)

# 2. 构造新文件名
for i in file_list:
    if flag == 1:
        new_name = 'Python_' + i
    elif flag == 2:
        num = len('Python_')      # replace()方法：替换字符串中的某个字符
        new_name = i[num:]

# 3. 重命名
    os.rename(i, new_name)