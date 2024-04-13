# numpy环境测试
import numpy as np
# 创建数组
a=np.arange(10)
print(a)
print(type(a))

# 对ndarray对象类型进行向量处理
print(np.sqrt(a))



# 对列表开平方
import math
b=[3,7,9]
# 定义存储开平方的列表
result=[]
for i in b:
    result.append(math.sqrt(i))
print(result)