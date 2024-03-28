ten_thing = 'Apple Orange Crows Telephone Light Sugar'

print('Wait there are not 10 things in that list. Let\'s fix that.')

stuff = ten_thing.split(' ')
more_stuff = ['Day','Night','Song','Frisbee','Corn','Banana','Girl','Boy']

while len(stuff) != 10:             # 只要stuff的长度不等于10，就一直循环
    next_one = more_stuff.pop()     # pop()函数，移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
    print('Adding:', next_one)
    stuff.append(next_one)
    print(f'There are {len(stuff)} items now.')

print('There we go:', stuff)

print('Let\'s do some things with stuff.')

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))         # join()是一个字符串方法，它用于将序列中的元素以指定的字符连接生成一个新的字符串
print('#'.join(stuff[3:5]))