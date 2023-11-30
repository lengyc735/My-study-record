"""
break 终止循环
continue 退出当前一次循环进而继续下一次循环
"""

# 吃5个火龙果，吃3个就吃不下了
i = 1
while i <= 5:
    if i >3:
        print('吃不下了，不吃了')
        break
    print(f'吃了{i}个火龙果')
    i += 1

# 吃5个苹果，第三个坏了不能吃
i = 1
while i < 6:
    if i == 3:
        print('这个是坏苹果吃不了')
        i += 1              # 必须先修改计数器，不然会陷入死循环
        continue
    print(f'吃了第{i}个苹果')
    i += 1
