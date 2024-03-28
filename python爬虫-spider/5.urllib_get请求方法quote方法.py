import urllib.request, urllib.parse

url = 'https://www.baidu.com/s?wd='
# wd 后直接跟汉字无法运行 需要进行转码

# 请求对象的定制为了解决反爬的第一种手段
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
}

# 将周杰伦3个字转换为unicode
# 需要依赖urllib.parse
name = urllib.parse.quote('周杰伦')

url = url + name

# 请求对象的定制
request = urllib.request.Request(url,headers=headers)

# 模拟浏览器向服务器发送数据
response = urllib.request.urlopen(request)

# 获取响应内容
content = response.read().decode('utf-8')

print(content)
