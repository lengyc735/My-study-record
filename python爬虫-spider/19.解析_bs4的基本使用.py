
from bs4 import BeautifulSoup


# 默认打开文件的编码格式是gbk 所以在打开文件的时候需要指定编码
# soup = BeautifulSoup(open('test.html',encoding= 'utf-8'),'lxml')

# 根据标签名查找节点
# 找到的是一个符和条件的数据
# print(soup.a)

# 获取标签的属性和属性值
# print(soup.a.attrs)

# bs4的一些函数

'''(1)'''
# 1.find        

# 返回第一个符和条件的数据
# print(soup.find('a'))

# 根据title的值来找到对应标签对象
# print(soup.find('a',title = 'a2'))

# 根据class的值来找到对应的标签对象 注意class是一个关键字 后面要加下划线_\
# print(soup.find('a',class_ = 'a1'))

'''(2)'''
# 2.find_all

# 返回所有符和条件的数据
# print(soup.find_all('a'))

# 如果想要获取的是多个标签的数据 那么需要在find_all中传入一个列表
# print(soup.find_all(['a','b']))

# limit参数限制返回的数据个数
# print(soup.find_all('a',limit = 2))


'''(3)'''
# 3.select

# select方法返回的是一个列表，并且会返回多个数据
# print(soup.select('a'))

# 可以通过.代表class 这种操作叫类选择器
# print(soup.select('.a1'))

# 通过#代表id 这种操作叫id选择器
# print(soup.select('#a1'))

# 层级选择器
# 后代选择器
# 找到的是div下面的li
# print(soup.select('div li'))

# 子代选择器
# 某标签的第一子标签
# 注意：很多的计算机编程语言 如果不加空格不会输出 但是在bs4中不会报错 会输出
# print(soup.select('div > ul > li'))

# 找到a标签和li标签的所有对象
# print(soup.select('a,li'))

# 节点信息
#    获取节点的内容
# obj = soup.select('a')[0]
# 如果标签对象中 只有内容 那么string和get_txt()都可以使用
# 如果标签对象中 有内容和标签 那么只能使用string
# 一般情况 使用get_txt()
# print(obj.string)
# print(obj.get_txt())

# 节点的属性
# obj = soup.select('#p1')[0]
# name是标签的名字
# print(obj.name)
# 将属性值作用一个字典返回
# print(obj.attrs)

# 获取节点的属性(三种方法)
# obj = soup.select('#p1')[0]
# print(obj['class'])
# print(obj.get('class'))
# print(obj.get('class'))