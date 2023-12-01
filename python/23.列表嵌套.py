name_list = [['小米','华为','欧珀'],['x','y','z'],['张张','牛牛','猪猪']]
print(name_list[0])
print(name_list[2][1])


# 分配7位老师到3间办公室
import random
teachers = ['a','b','c','d','e','f','g']
offices = [[],[],[]]
for name in teachers:
    # 列表追加数据：append(追加整体) extend(拆开追加个体) insert(指定位置追加)
    num = random.randint(0,2)
    offices[num].append(name)
print(offices)
i = 1
for office in offices:
    print(f'办公室{i}人数为{len(office)},老师分别是：')
    for name in office:
        print(name)
    i += 1
