# “下标”又叫“索引”，就是编号

str1 = 'abcdefg'
print(str1)

# 数据在程序运行过程中存储在内存
# 如何使用字符串中某个特定的数据
# 这些数据从0开始顺序分配一个编号--用编号即可快速找到想要的数据-- 下标 或 索引 或 索引值
# str[下标]
print(str1[2])
print(str1[0])    # 注意第一个值是0 不是1
print(type(str1[2]),type(str1[0]))

# 切片
'''
切片是指对操作对象截取其中一部分的操作， 字符串，元组，列表都支持切片

语法：
序列[开始下标位置:结束下标位置:步长]

注意:1.不包含结束位置下标对应的数据，正负整数均可；
     2.步长是选取间隔,正负整数均可,默认值为1
'''
str2 = '012345678'
print(str2[2:5:1])    #234
print(str2[0:7:2])    #0246
print(str2[:5])       #01234   不写开始默认为0 不写步长默认为1
print(str2[2:])       #2345678   不写结束默认到最后
print(str2[:])        #012345678   为本体

# 负数
print(str2[::-1])    #876543210   选取所有值，并且倒序选取
print(str2[-4:1])    #567   下标-1表示最后一个值

print(str2[-4:-1:1])  #567
#print(str2[-4:-1:-1]) 不能选取 ，从-4到-1是从左到右取，步长-1是从右开始取，两者矛盾
# 如果选取方向(下标开始到结束的方向) 和 步长的方向冲突，则无法选取数据
print(str2[-1:-4:-1])  #876