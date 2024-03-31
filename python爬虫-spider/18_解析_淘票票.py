import urllib.request

url = "https://www.taopiaopiao.com/showAction.json?_ksTS=1711877966796_64&jsoncallback=jsonp65&action=showAction&n_s=new&event_submit_doGetSoon=true"

headers = {
    'authority': 'www.taopiaopiao.com',
    #':method': 'GET',
    #':path': '/cityAction.json?city=&_ksTS=1711877966520_19&jsoncallback=jsonp20&action=cityAction&n_s=new&event_submit_doLocate=true',
    #':scheme': 'https',
    'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    #'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6,en-GB;q=0.5',
    'Cookie': 'isg=BMTEsA3bfr51vMryoUkRwth9lUK23ehH0Lr7k95n-Q9SCWXTBu8h1iDqSaHRESCf',
    'Referer': 'https://www.taopiaopiao.com/?tbpm=3',
    'Sec-Ch-Ua': '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
}

request = urllib.request.Request(url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

#print(content)

content = content.split('(')[1].split(')')[0]

with open('18.解析_淘票票.json','w',encoding='utf-8') as f:
    f.write(content)

import json
import jsonpath
obj = json.load(open('18.解析_淘票票.json','r',encoding = 'utf-8'))

# 通过jsonpath提取数据
show_list = jsonpath.jsonpath(obj,'$..showName')
print(show_list)