# help函数作用：查看函数的说明文档(函数的解释说明的信息)
help(len)

'''
语法：

定义函数说明文档

def 函数名(参数):
    """ 说明文档位置 """      # 注意：只能写在函数内部第一行
    代码
    ...

查看函数的说明文档

help(函数名)
'''

def qm_num(a,b):
    """ 求幂函数 """
    return a ** b

help(qm_num)

# 说明文档 进阶用法

def sum_num(a,b):
    """
    求和函数
    a:参数一
    b：参数二
    return：返回值
    """
    return a + b

help(sum_num)