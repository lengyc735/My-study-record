people = 20
cats = 30
dogs = 15

if people < cats:
    print("too many cats! the world is doomed!")

if people > cats:
    print("Not many cats! the world is saved!")

if people < dogs:
    print('The world is drooled on!')

if people > dogs:
    print('The world is dry!')

dogs += 5

if people >= dogs:
    print('People are greater than or equal to dogs.')

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print('People are dogs.')

'''
在Python中，缩进是用来表示代码块的开始和结束的。if 语句后面的代码块需要缩进，以表示这些代码只有在 if 条件为 True 时才会执行

缩进可以是任何数量的空格，但是Python的官方风格指南PEP 8建议使用4个空格的缩进。这是为了保持代码的一致性和可读性
'''