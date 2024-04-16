import matplotlib.pyplot as plt
# 准备x y
x=range(-100,100) # 200个点
y=[i**2 for i in x]
# 绘制一元二次方程曲线
plt.plot(x,y)
# 保存图片
plt.savefig('4.result.jpg')  # 格式默认png
plt.show()