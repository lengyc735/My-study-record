# post请求

import urllib.request, urllib.parse

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
}

data = {
    'kw':'spider'
}

# post请求的data数据需要进行编码
# 必须将data变成字节型
data = urllib.parse.urlencode(data).encode('utf-8')

# post的请求参数 是不会拼接在url后面的 而是放在请求对象定制的参数中
request = urllib.request.Request(url,data=data,headers=headers)

# 模拟浏览器想服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应数据
content = response.read().decode('utf-8')

# 字符串-->> json对象

import json

obj = json.loads(content)
print(obj)