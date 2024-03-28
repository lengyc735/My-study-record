animal = ['bear', 'tiger', 'penguin', 'aebra' , 'kangaroo', 'whale', 'platypus']
a = [1, 2, 3, 4, 5, 6, 7]

# 按顺序打印动物
for i, j in zip(animal, a):           # zip()函数可以将多个列表合并成一个元组列表
    if j == 7:
        print('第{j}只动物是最后一只了，它是{i}'.format(j=j, i=i))  # format()函数可以将字符串中的占位符替换成变量,format前应该有一点'.'
    else:
        print(f'列表animal的第{j}个动物是{i}')