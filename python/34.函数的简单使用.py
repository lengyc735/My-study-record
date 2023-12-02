'''
1.定义函数
def 函数名(参数):
    代码1
    代码2
    ...
注意：函数名是自定义的
'''

'''
2.调用函数
函数名(参数)
注意：1.不同需求，参数可有可无；2.在python中，函数必须*先定义后使用*
'''

# 例子： 复现atm取钱功能

# 因为函数要先定义再调用，所以2和3要在1的上面

# 2.确定功能界面:显示余额，存款，取款   # 3.封装函数
def sel_func():
    print('显示余额')
    print('显示存款')
    print('显示取款')

# 1.搭建整体框架
'''
输入密码登录后显示功能：查询余额后显示功能：取完钱后显示功能
'''
print('恭喜您登陆成功')
#显示功能界面  # 4.在需要的位置调用函数
sel_func()

print('您的余额为771777779')
#显示功能界面  # 4.在需要的位置调用函数
sel_func()

print('您取了100元钱')
#显示功能界面  # 4.在需要的位置调用函数
sel_func()

