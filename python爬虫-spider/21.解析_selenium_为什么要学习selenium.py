
import urllib.request

url = 'https://miaosha.jd.com/'

response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')

print(content)

# 搜索J-superkillGoodslist发现不存在
# 会检测是不是浏览器访问，如果不是浏览器访问，就会返回一个空的页面