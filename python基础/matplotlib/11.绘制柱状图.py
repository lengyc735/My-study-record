import matplotlib.pyplot as plt
import numpy as np
# 创建x,y 表示年份x 表示年份对应的销量
x=[1980,1985,1990,1995]
x_label=['1980年','1985年','1990年','1995年']
y=[1000,3000,4000,5000]
# 调用bar函数绘制柱状图
plt.bar(x,y,width=3)   # width修改宽度
# 调整中文乱码
plt.rcParams['font.sans-serif']=['SimHei']  # 用来正常显示中文
# 修改x坐标的值
plt.xticks(x,x_label)
# 添加xy坐标名称
plt.xlabel('年份')
plt.ylabel('销量')
# 添加标题
plt.title('根据年份销量对比')
plt.show()