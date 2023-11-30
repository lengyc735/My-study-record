"""
if 条件：
    条件成立执行的代码1
    ......
"""

if True:
    print('条件成立执行的代码1')     # 开头要缩进4个字符
    print('条件成立执行的代码2')     # 假如符和if的条件就会被输出
print('这行代码执行吗？')

if False:
    print('条件成立执行的代码1')     # 条件不成立所以13，14行代码不执行 
    print('条件成立执行的代码2')
 # 注意：在这个下方的没有加缩进的代码，不属于if语句块，即和条件成立与否无关
print('无论条件成立与否，这条代码都执行')

# 简单举例
age = 19
if age >= 18:
    print('您已成年，可以上网')
print('系统正在关闭')

# 进阶举例
age = int(input('请输入您的年龄：'))
#input接受用户输入的数据是字符串，条件是age和18的整形做判断，所以这里要用int转换数据类型
if age >= 18:
    print(f'您的年龄是{ age}，已经成年，可以上网')
print('系统正在关闭')

"""
if 条件语块：
    条件成立执行的代码1
    条件成立执行的代码2
    .......
else:         注:不满足条件语块的执行else下的代码
    条件不成立执行的代码1
    条件不成立执行的代码2
    ......
"""

# 举例
age = int(input('请输入您的年龄：'))
if age >= 18:
    print(f'您的年龄是{age},已经成年，可以上网')
else:
    print(f'您的年龄是{age}，小朋友，未成年不可以上网')
print('系统正在关闭')

# 注意：如果某些条件成立执行了相关代码，那其他情况的代码解释器不会执行
"""
if 条件语块：
    条件成立执行的代码1
    条件成立执行的代码2
    .......
elif:         
    条件成立执行的代码1
    条件成立执行的代码2
    ......
 ......      #可以有多个elif存在
 else:
    以上条件都不成立的条件执行的代码
"""
age = int(input('请输入您的年龄：'))
if age < 18:
    print(f'您输入的年龄是{age},是童工，不合法')
elif age >= 18 and age <= 60:    # 等效于 18 <= age <= 60
    print(f'您输入的年龄是{age},为合法工作年龄')
else:
    print(f'您输入的年龄是{age},为退休年龄')
