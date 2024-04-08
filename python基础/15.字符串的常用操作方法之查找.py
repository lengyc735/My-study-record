# 字符串的常用操作方法
#常用方法：查找,修改，判断三大类

# 查找
# find():检测某个子串是否包含在这个字符串中，如果在返回这个子串开始的位置下标，否则则返回-1
"""语法：
字符串序列.find(子串,开始位置下标,结束位置下标)
注意:开始和结束位置下标可以省略，表示在整个字符串序列中查找。 
"""

mystr = 'hellow world and itcast and itheima and python'

# 1.find
print(mystr.find('and'))            # 13
print(mystr.find('and',15,30))      # 24
print(mystr.find('ands'))           # -1

# 2.index    注：用法与find类似
print(mystr.index('and'))           # 13
print(mystr.index('and',15, 30))    # 24
#print(mystr.index('ands'))          如果index查找子串不存在，会报错

# 3.count  注：count返回结果为出现次数
print(mystr.count('and',15,30))     # 1
print(mystr.count('and'))           # 3
print(mystr.count('ands'))          # 0

"""
rfind(): 和fing功能一样，但查找方向为右侧开始
rindex(): 和index()功能一样，但查找方向为右侧开始
"""
