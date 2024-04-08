# 用户输入文件
old_name = input('请输入您要备份的文件名： ')
print(old_name)


# 2.规划备份文件名字
# 2.1 提取后
# 2.2 组织新名字 旧文件名字+【备份】+后缀

index = old_name.rfind('.')   # 从右边开始找

# 注意：控制文件名字的输入，防止用户输入错误
if index > 0:
    postfix = old_name[index:]

print(old_name[:index])     # 用切片找到旧文件名
print(old_name[index:])     # 用切片找到后缀名

new_name = old_name[:index] + '[备份]' + postfix   # 如果用户输入的文件名没有后缀，会报错
print(new_name)

# 3.备份文件写入数据
# 3.1 打开 原文件 和 备份文件 文件

old_f = open(old_name,'rb')
new_f = open(new_name,'wb')

# 3.2 读取 原文件 内容，写入到 备份文件
# 如果不确定文件大小，可以循环读取写入
while True:
    con = old_f.read(1024)
    if con == 0:
        # 读取完成
        break

# 3.3 关闭 2 个文件
old_f.close()
new_f.close()