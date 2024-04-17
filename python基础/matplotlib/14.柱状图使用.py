import matplotlib.pyplot as plt
import numpy as np

# 电影名
real_names=['言叶之庭','你的名字','天气之子']
# 3天内票房
real_num1=[7673,4343,3213]
real_num2=[4532,3421,2321]
real_num3=[3231,2412,1342]
x=np.arange(len(real_names))
#  绘制柱状图
width=0.3
plt.bar(x,real_num1,alpha=0.5,width=width,label=real_names[0])
plt.bar([i+width for i in x],real_num2,alpha=0.5,width=width,label=real_names[1])
plt.bar([i+2*width  for i in x],real_num3,alpha=0.5,width=width,label=real_names[2])
plt.rcParams['font.sans-serif']=['SimHei']
# 设置x的坐标的值 第1天 第2天 第3天
x_label=['第{}天'.format(i+1) for i in x]
plt.xticks([i+width for i in x],x_label)
# 添加ylabel
plt.ylabel('票房数')
# 添加图例
plt.legend()
# 添加标题
plt.title('3天内票房数')
plt.show()