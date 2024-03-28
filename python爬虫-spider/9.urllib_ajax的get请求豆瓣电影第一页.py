# 爬取豆瓣第一页(get)

import urllib.request

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
}

request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# print(content)

# 将爬取的数据保存到文件中 方法1
# fi = open('9.douban.json','w',encoding='utf-8')
# fi.write(content)
# fi.close()

# 方法2
with open('9.douban.json','w',encoding='utf-8') as fi:
    fi.write(content)