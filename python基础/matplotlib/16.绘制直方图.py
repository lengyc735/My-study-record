import matplotlib.pyplot as plt
import numpy as np
# 生成1000个标志的正态分布随机数
x=np.random.randn(1000)
# plt.hist(x)
# 修改柱的宽度 使用bins
plt.hist(x,bins=100) # 10个柱装在一起
plt.show()