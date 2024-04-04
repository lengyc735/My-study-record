
import requests

url = 'https://www.bing.com/search'

headers = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
}

data = {
    'q': '厦门'
}

# request.get(url,params=None,**kwargs)
# url: 请求的url地址
# params: 请求的参数
# **kwargs: 可选参数(字典)
response = requests.get(url,params=data,headers=headers)

content = response.text

print(content)

# 总结
# 1.参数使用params传递
# 2.无需urlencode编码
# 3.不需要请求对象的定制
# 4.请求资源路径的？可以删除或保留