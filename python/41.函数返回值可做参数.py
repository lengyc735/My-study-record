# 返回值做参数
def test_1():
    return 77

result = test_1()

def test_2(num):
    print(num+1)

test_2(result)

# 多个返回值
def test3():
    return 1, 2  # 返回类型默认为元组
    # return 后面可以直接书写 元组 列表 字典， 返回多个值

result = test3()
print(result)  