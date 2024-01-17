"""
递归的特点
1.函数内部自己调用自己
2.必须有出口
"""

def sum_nums(num):
    """求累加和"""
    if num == 1:
        return 1
    return num + sum_nums(num-1)

result = sum_nums(3)
print(result)