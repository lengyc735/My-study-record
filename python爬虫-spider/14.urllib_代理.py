'''
代理常用功能：
1.隐藏真实IP地址
2.访问限制网站
3.提高访问数据
'''

import urllib.request

url = 'https://www.whatismyip.com.tw/'

headers = {
     'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
}

# 请求对象的定制
request = urllib.request.Request(url=url,headers=headers)

# 模拟浏览器访问地址
#response = urllib.request.urlopen(request)

proxies = {
    'http':'62.210.9.0:443'
}

# handler build_opener  open
handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

# 获取响应数据
content = response.read().decode('utf-8') 

# 保存数据
with open('14.代理测试.html','w',encoding='utf-8') as fp:
    fp.write(content)