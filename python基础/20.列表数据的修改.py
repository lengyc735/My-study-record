# 1.修改指定下标的数据
list_1 = ['121','wiwii','8889']
list_1[2] = '777'
print(list_1)

# 2.reverse() 逆序函数
list_2 = [1,2,3,4,5,6]
list_2.reverse()
print(list_2)
'''
3.sort() 排序：升序(False) 和 降序(True)
列表序列.sort( key=None, reverse=False)
注意:reverse表示排序规则，reverse = True 降序，reverrse = False 升序(默认)
'''
list_3 = [2,3,7,5,2,9,0]
list_3.sort()          #默认为升序
print(list_3)

list_4 = [2,4,7,8,4,3,1,0]
list_4.sort(reverse=True)
print(list_4)