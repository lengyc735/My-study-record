import numpy as np

def randomTest():
    # 使用random创建一维数组
    a=np.random.random(size=5)
    print(a)
    print(type(a))

    # 创建二维数组
    b=np.random.random(size=(3,4))
    print(b)

    # 创建三维数组
    c=np.random.random(size=(2,3,4))
    print(c)


# 随机整数
def randintTest():
    # 0-5 一维
    a=np.random.randint(6,size=10)
    print(a)
    print(type(a))

    # 5-10 二维
    b=np.random.randint(5,11,size=(4,3))
    print(b)

    # 5-10 三维
    c=np.random.randint(5,11,size=(2,4,3))
    print(c)

    # dtype
    d=np.random.randint(10,size=5)
    print('默认的dtype',d.dtype)

def randnTest():
    '''标准正态分布样本-->期望为0，方差为1'''
    a=np.random.randn(4)
    print(a)

    # 二维
    b=np.random.randn(2,3)
    print(b)

    # 三维
    c=np.random.randn(2,3,4)
    print(c)

def normalTest():
    '''创建指定期望和方差的正太分布'''
    # 一维
    a=np.random.normal(size=5)  # 默认是期望loc=0.0, 方差scale=1.0
    print(a)

    #指定期望和方差
    b=np.random.normal(loc=2,scale=3,size=(3,4))
    print(b)

#randomTest()
#randintTest()
#randnTest()
normalTest()