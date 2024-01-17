# 缺省参数 又叫默认参数

def user_info(name, age, gender='男'):
    print(f'您的名字是{name},您的年龄是{age},您的性别是{gender}')

user_info('lily',21)
user_info('Tom',22,'女')

# 注意：函数调用时。如果为缺省参数传值则修改默认参数值，否则使用这个默认值
# 位置参数必须写在默认参数之前


# 不定长参数 又叫可变参数

# 包裹位置传递
def user_info2(*args):
    print(args)

user_info2('tom')
user_info2('tom',18,'男')
# 传进的所有参数都会被args变量收集，他会根据传进参数的位置合并为一个 元组

# 包裹关键字传递 （返回字典）
def user_info3(**kwargs):
    print(kwargs)

user_info3(name='lily',age=23,id=112)

# 无论包裹位置传递还是包裹关键字传递，都是一个组包的过程