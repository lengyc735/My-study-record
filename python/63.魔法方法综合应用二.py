# 搬家案例

class Furniture():
    def __init__(self,name,area):
        # 家具的名字
        self.name = name
        # 家具占地面积
        self.area = area


class Home():
    def __init__(self,address,area):
        # 房子的地址
        self.address = address
        # 房子的面积
        self.area = area
        # 房子剩余面积
        self.free_area = area
        # 家具列表
        self.furniture = []

    def __str__(self):
        return f'''房子的地址是{self.address},占地面积{self.area},
        剩余面积{self.free_area},家具有{self.furniture}'''

    def add_furniture(self,item):
        '''容纳家具'''
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            # 剩余面积 = 之前剩余面积 - 家具面积
            self.free_area -= item.area
        else:
            print('家具太大了，没地方放了')


bed = Furniture('席梦思',4)
jia1 = Home('北京',120)
print(jia1)

jia1.add_furniture(bed)
print(jia1)

sofa = Furniture('沙发',10)
jia1.add_furniture(sofa)
print(jia1)