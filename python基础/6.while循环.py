"""
       【while循环的语法】
while 条件：
    条件成立重复执行的代码1
    条件成立重复执行的代码2
    ......
"""

# 需求：说5次我爱你
i = 1
while i <= 5:
    print('我爱你')
    i += 1
print('我也爱你')

# 应用1：1-100的累加和
i = 1
result = 0
while i <= 100:
    result += i
    i += 1
print(result)

# 应用2：1-100的偶数的累加和
#方法【1】 更推荐使用！
i = 1
result = 0 
while i < 101:
    if i % 2 ==0:
        result += i
    i += 1
print(result)

#方法【2】
i = 2
result = 0 
while i <= 100:
    result += i
    i += 2
print(result)
