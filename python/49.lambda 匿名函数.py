# lambda 匿名函数

fn1 = lambda: 100
print(fn1)  # 此时的输出为lambda的内存地址
print(fn1())  # 100

# 计算a+b

fn2 = lambda a, b: a + b
print(fn2(1,3))

"""
lambda参数
1·无参数
2·一个参数
3·默认参数
4·可变参数
"""

# 可变参数

fn2 = lambda *args: args
print(fn2(10,20,30))
# 注意这里返回值为元组

fn3 = lambda **kwargs: kwargs
print(fn3(name='leng',age=18))
# 此处返回值为字典

# lambda 应用

fn4 =  lambda a, b: a if a > b else b
print(fn4(1000,500))

# 列表数据排序
students = [{'name':'Tom','age':18},{'name':'Lily','age':19},{'name':'Kobe',"age":20}]

# 按name值升序排序
students.sort(key=lambda x: x['name'])
print(students)

# 按name值降序排列
students.sort(key=lambda x: x['name'], reverse=True)
print(students)
