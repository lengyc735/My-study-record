# 对数值排序
sort_list1=sorted([36, 5, -12, 9, -21])
print('默认升序排序：',sort_list1)

sort_list2=sorted([36, 5, -12, 9, -21],key=abs)
print('按绝对值升序排序：',sort_list2)

sort_list3=sorted([36, 5, -12, 9, -21],key=abs,reverse=True)
print('按绝对值降序排序：',sort_list3)

# 对字符串排序 根据ASCII码排序 A:65 Z:90 a:97 z:122
sort_list4=sorted(['bob', 'about', 'Zoo', 'Credit'])
print('默认ASCII码升序排序：',sort_list4)

sort_list5=sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower)
print('忽略大小写排序：',sort_list5)

sort_list6=sorted(['bob', 'about', 'Zoo', 'Credit'],reverse=True)
print('降序排序：',sort_list6)