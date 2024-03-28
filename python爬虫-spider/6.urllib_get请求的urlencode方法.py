# urlencode应用场景： 传递多个参数的时候

# https://www.baidu.com/s?wd=周杰伦&sex=男

# 测试代码

# import urllib.parse
# data = {
#     'wd':'周杰伦',
#     'sex':'男',
#     'location':'中国台湾省'
# }
# a = urllib.parse.urlencode(data)
# print(a)

import urllib.request, urllib.parse

base_url = 'https://www.baidu.com/s?'

data = {
    'wd':'周杰伦',
    'sex':'男',
    'location':'中国台湾省'
}

new_data = urllib.parse.urlencode(data)

# 请求资源路径
url = base_url + new_data

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
}

# 请求对象的定制
request = urllib.request.Request(url=url ,headers=headers)

# 模拟浏览器向服务器发送数据
response = urllib.request.urlopen(request)

#获取网页源码数据
content = response.read().decode('utf-8')

print(content)