# 位置参数
def user_info(name,age,gender):
    print(f'您的名字是{name},您的年龄是{age},您的性别是{gender}')

user_info('leng',20,'男')

# 注意：传递和定义参数的顺序及个数必须一致

# 关键字参数
user_info('Rose',age=20,gender='wu')
user_info('lily',gender='女',age=21)

# 注意：位置参数不能出现在关键粗参数之后