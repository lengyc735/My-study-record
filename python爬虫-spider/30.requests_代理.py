
import requests

url = 'https://www.myip.com/'

headers = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
}

# data = {
#     'wd': 'ip'
# }

proxy = {
    'http': '85.114.138.102:443'
}


response = requests.get(url,headers=headers,proxies=proxy)

content = response.text


# 测试服务器是否可用
try:
    response = requests.get(url, headers=headers, proxies=proxy, timeout=5)
    print('代理服务器可用')
except requests.exceptions.RequestException as e:
    print('代理服务器不可用')


with open('30.代理测试.html','w',encoding='utf-8') as f:
    f.write(content)