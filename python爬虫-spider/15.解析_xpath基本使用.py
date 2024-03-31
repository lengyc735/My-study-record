from lxml import etree
import urllib.request

# xpath解析
# (1) xlml.parse 
#      解析本地文件
# (2) xlml.HTML 
#    解析网络数据(服务器响应的数据) response.read().decode('utf-8')

# 解析本地文件
'''
tree = etree.parse('test.html')
print(tree)

li = tree.xpath('//li/text()')

查询id中包含l的li标签
li = tree.xpath('//li[contains(@id,"l")]/text()')
'''

# 解析网络数据
# 获取服务器响应文件
response = urllib.request.urlopen('http://www.baidu.com')
html = response.read().decode('utf-8')

# 解析服务器响应文件
tree = etree.HTML(html)

# 获取想要的数据 xpath返回的数值是一个列表
result = tree.xpath('//input[@id="su"]/@value')[0]
print(result)  # 百度一下