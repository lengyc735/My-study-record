import urllib.request

url = 'http://www.baidu.com'

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 一个类型和六个方法

# 一个类型 HTTPResponse
# 六个类型 read readline readlines getcode geturl getheaders

'''
print(type(response))
# <class 'http.client.HTTPResponse'>
# response是一个HTTPResponse类型的对象
'''

'''
content = response.read()
print(content)
按照一个字节一个字节去读取
'''

'''
content = response.read(5)
print(content)
返回多少字节
'''

'''
content = response.readline()
print(content)
按行读取
'''

'''
content = response.readlines()
print(content)
'''

'''
返回状态码  如果是200 说明请求成功
print(response.getcode())
'''

'''
返回url地址
print(response.geturl())
'''

'''
获取一个状态信息
print(response.getheaders())
'''
