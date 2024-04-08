#  考地瓜

class Sweetpotato():
    def __init__(self):
        # 被烤的的时间
        self.cook_time = 0
        # 地瓜的状态
        self.cook_static = '生的'
        # 调料列表
        self.condiments = []

    def cook(self,time):
        '''考地瓜的方法'''
        # 1.先计算地瓜整体烤过的时间
        self.cook_time += time
        # 2.用整体的时间判断地瓜的状态
        if 0 <= self.cook_time < 3:
            self.cook_static = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_static = '半生不熟'
        elif 5 <= self.cook_time < 8:
            self.cook_static = '熟了'
        elif self.cook_time >= 8:
            self.cook_static = '烤糊了'
        
    def add_condiments(self,condiment):
        '''添加调料'''
        self.condiments.append(condiment)

    def __str__(self):
        return f'这个地瓜烤了{self.cook_time}分钟，状态是{self.cook_static},调料有{self.condiments}'



# 1.创建一个地瓜对象调用对应的实例方法
    
digua1 = Sweetpotato()

print(digua1)

digua1.cook(2)
digua1.add_condiments('辣椒')
print(digua1)