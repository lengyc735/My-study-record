# 注意 jsonpath只能解析本地文件，不能解析url

import json
import jsonpath

obj = json.load(open('17.解析_jsonpath.json','r',encoding = 'utf-8'))
# print(obj)

# 通过jsonpath提取数据
# 提取所有书的author
author_list = jsonpath.jsonpath(obj,'$.store.book[*].author')
# 提取第一本书的author
author_1 = jsonpath.jsonpath(obj,'$.store.book[0].author')
print(author_list)
print(author_1)

# 获取所有的author，包括书之外的
all_author = jsonpath.jsonpath(obj,'$..author')
print(all_author)

# store 下的所有元素
tag_list = jsonpath.jsonpath(obj,'$.store.*')
#print(tag_list)

# store 下的所有元素的price
price_list = jsonpath.jsonpath(obj,'$.store..price')
print(price_list)

# 最后一本书
last_book = jsonpath.jsonpath(obj,'$..book[(@.length-1)]')
#print(last_book)

# 条件过滤 需要在()前加?
# 含有isbn的元素
isbn_list = jsonpath.jsonpath(obj,'$..book[?(@.isbn)]')
#print(isbn_list)

# price大于10的元素
ten_price = jsonpath.jsonpath(obj,'$..book[?(@.price>10)]')
#print(ten_price)