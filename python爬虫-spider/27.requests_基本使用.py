
import requests

url = 'http://www.baidu.com'

response = requests.get(url)

# 设置响应的编码格式
response.encoding = 'utf-8'


# 一个类型和六个属性

# Response对象的类型是<class 'requests.models.Response'>
# print(type(response))

# 以字符串的形式返回了网页源码
# print(response.text)

# 返回路径
# print(response.url)

# 返回二进制的数据
# print(response.content)

# 返回状态码
# print(response.status_code)

# 返回响应头
# print(response.headers)