# 仅保留列表的奇数
def is_odd(n):
    return n % 2 == 1
L=filter(is_odd,[1,2,3,4,5,6,7,8,9])
print(list(L))

# 去掉列表中的空字符串
def not_empty(s):
    return s and s.strip()
L2=filter(not_empty,['A','B',' ',None,'C',''])
print(list(L2))