import matplotlib.pyplot as plt
import numpy as np
# 生成0-10之间 100个等差数
x=np.linspace(0,10,100)
sin_y=np.sin(x)
# 进行绘制正弦曲线
plt.plot(x,sin_y)
# 余弦
cos_y=np.cos(x)
plt.plot(x,cos_y)
plt.show()