'''
1.异常：

语法：
try:
    可能发生错误的代码
except:
    如果发生错误执行的代码

'''

try:
    print(1/0)
except:
    print('除数不能为0')


'''
2.捕获指定异常：

语法：
try:
    可能发生错误的代码
except 异常类型:
    如果捕获到该异常类型执行的代码
'''

try:
    print(num)
except NameError:
    print('\n有错误')

'''
注意：
  1. 如果尝试执行的代码的异常类型和要捕获的异常类型不一致，则无法捕获异常
  2.一般try下方只放一行尝试执行的代码
'''


# 3.捕获多个指定异常：
try:
    print(1/0)
except (NameError, ZeroDivisionError):
    print('\n有有错误')


# 4.捕获异常描述信息
try:
    print(1/0)
except (NameError,ZeroDivisionError) as result:
    print(result)


# 5.捕获所有异常
# Exception是所有程序异常类的父类，所以在捕获异常时，它能够捕获到所有的异常
try:
    print(num)
except Exception as reason:
    print(reason)

# 6.else
try:
    print(1)
except Exception as reason:
    print(reason)
else:
    print('\n我是else，是没有异常时执行的代码')    


# 7.finally
# 无论是否捕获到异常，finally中的代码都会执行
try:
    print(1)
except Exception as reason:
    print(reason)
else:
    print('芜湖，没有异常')
finally:
    print('我是finally，我一定会被执行')