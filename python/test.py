import random
restaurant = ['万人','西苑','清真','诚毅']
random_restaurant = random.choice(restaurant)
print(f'我要去{random_restaurant}吃')
if random_restaurant == '万人':
    dishes_wr = ['就吃饭吧','来碗牛肉粉吧','石锅饭烫嘴巴','冬粉鸭没一点味','杂酱面有吗','狗都不吃的减脂餐']
    r_dishes_wr = random.choice(dishes_wr)
    print(r_dishes_wr)
elif random_restaurant == '西苑':
    dishes_xy = ['爆辣水煮小鲜肉','桂林拌米粉加粉','没灵魂的拌泡面','螺蛳粉加炸蛋','爆辣水煮毛血旺']
    r_dishes_xy = random.choice(dishes_xy)
    print(r_dishes_xy) 
elif random_restaurant == '清真':
    dishes_qz = ['来豌碗碗碗杂面','吃了想呕的二楼牛肉面','爆chao炒面','爆辣辣辣抄手','狗都不吃的饺子']
    r_dishes_qz = random.choice(dishes_qz)
    print(r_dishes_qz)
else:
    # 牛魔的诚毅没去吃过几次，不知道有啥
    window_cy = random.randint(1,17)
    print(f'去{window_cy}号窗口看看吧') 
