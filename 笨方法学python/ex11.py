print("How old are you",)
age = input()             #input()函数接受一个标准输入数据，返回为 string 类型。    python2 是raw_input()
print("How tall are you",)
height = input()
print("How much do you weight?",)
weight = input()

print("So, you're %r old, %r tall and %r heavy." % (age, height, weight))