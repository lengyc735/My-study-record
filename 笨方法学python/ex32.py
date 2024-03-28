the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'bananas']
change = [1, 'pennies', 2 , 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list  第一种类型的for循环遍历一个列表
for number in the_count:
    print(f"This is count {number}")

# same as above  同上
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too  我们也可以遍历混合列表
# notice we have to use {} since we don't know what's in it  注意我们必须使用{}，因为我们不知道里面有什么
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one  我们也可以构建列表，首先从一个空列表开始
elements = []

# then use the range function to do 0 to 5 counts  然后使用范围函数进行0到5次计数
for i in range(0,6):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand.   append是列表理解的函数
    elements.append(i)

# now we can print them out too  现在我们也可以打印出来
for i in elements:
    print(f"Element was: {i}")