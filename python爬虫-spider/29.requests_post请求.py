
import requests

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
}

data = {
    'kw': 'damn'
}

response = requests.post(url,data=data,headers=headers)

content = response.text

import json

obj = json.loads(content)
print(obj)

print(content)


# 总结
# 1.post请求 不需要编码
# 2.post请求参数是data
# 3.不需要请求对象的定制