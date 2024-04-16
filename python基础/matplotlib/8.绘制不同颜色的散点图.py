import matplotlib.pyplot as plt
import numpy as np

# 绘制10种大小 100种颜色的散点图
# 创建x
np.random.seed(0) # 执行多次每次获取的随机数都是一样的
x=np.random.rand(100)
y=np.random.rand(100)
# 生成10种大小
size=np.random.rand(100)*1000
# 生产100种颜色
color=np.random.rand(100)
# print(x)
# 绘制散点图
plt.scatter(x,y,s=size,c=color,alpha=0.7) # s表示点的大小 c表示点的颜色 alpha表示透明度
plt.show()