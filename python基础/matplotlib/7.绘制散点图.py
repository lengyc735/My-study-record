import matplotlib.pyplot as plt
import numpy as np
# 生成0-10之间100个等差数
x=np.linspace(0,10,100)
sin_y=np.sin(x)
# 绘制正弦曲线
plt.plot(x,sin_y,'o')
# 绘制散点图
# plt.scatter(x,sin_y)
plt.show()

'''
plot绘制和scatter绘制的图形没有差别
但是plot绘制速度优于scatter
如果绘制点的形式有差别(指点的大小和颜色不同)则必须使用scatter
'''