
import urllib.request, urllib.parse

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

# 注：此处的cookie起决定作用
headers = {
    'Accept': '*/*',
    #'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6,en-GB;q=0.5',
    'Acs-Token': '1711195205096_1711200703958_DetSfFXjbO15g1h2UXFPfCsswF4Q5Dqaog4VeLU9xwtlm4q6rB49cmjlenGsgl+iV1DwWMXkU43L8UunjfkCyn0/kcYKgBs+bSorpZr4DFg3tVzSaufkiL63TXWHiI1RJDJ161bfVF/Pnv0a147iZGQ905vQgtjaU4F+nX+yHOav1t6/IvqRPMts+2rF09Yq+Pjr3pWz3x3BzjL8EpE9EGRkwOv83B15as78c+I+PpzLG0ys8HC2equQDzJlOBmGD0sSx6+FVXH3JfVLcIG31pzpNca6Q2RiVKAKTFfz4vIAJdHoYy+bYsxXxNz3MfnCk1w7CGczopLXOVYcMsmA2KDSZUWBLl3BmXTU2BCZkJ7iSAlEJPhzqiY0QFtNMYapj1khDLAPJ8Q1UANW5ZxG4isV5DTeAv7Jycs8DTWZ32jEfXUxrcJ2b68qDWgy4tzqoHJpMN4UohSrii9xhK9rpADW+16kE7LzyVqz5kTYmlxZ38Euh6kKj6oge7aGoG21',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '152',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BIDUPSID=FFE133D813E20692DFF6D4352716969F; PSTM=1698541724; H_WISE_SIDS=40008_40016_40040; newlogin=1; BDUSS=BXOE5-d3N2b1JsQmRFSkJzRDBRSEVlWGIxUGw3RmpyYlJ4ZUs5VXlELTBmUWRtSVFBQUFBJCQAAAAAAQAAAAEAAAD-Wd8QZGV2aWzxq77919MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALTw32W08N9la1; BDUSS_BFESS=BXOE5-d3N2b1JsQmRFSkJzRDBRSEVlWGIxUGw3RmpyYlJ4ZUs5VXlELTBmUWRtSVFBQUFBJCQAAAAAAQAAAAEAAAD-Wd8QZGV2aWzxq77919MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALTw32W08N9la1; BAIDUID=26689A985D43E1B354432502E6C14515:FG=1; H_PS_PSSID=40210_40207_40224_40272_40295_40291_40287_40318_40080_40364_40352_40303; BAIDUID_BFESS=26689A985D43E1B354432502E6C14515:FG=1; BAIDU_WISE_UID=wapp_1709717177413_402; ZFY=xqX9\
        lkaM3dw8:AtGv23Rj16cJiHbJDA:BEQgkJP5mbVP0:C; RT="z=1&dm=baidu.com&si=4479d474-cdac-4e13-8aee-25cb1d61a050&ss=ltwhj1bt&sl=1i&tt=j1z&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=q3yd&nu=32vxb12i&cl=oqap&ul=q66o&hd=q67n"; APPGUIDE_10_7_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Pragma': 'no-cache',
    'Referer': 'https://fanyi.baidu.com/',
    'Sec-Ch-Ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
}

data = {
    'from': 'en',
    'to': 'zh',
    'query': 'love',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '198772.518981',
    'token': 'dfb49a98a674df4ed1f963c3c06e3119',
    'domain': 'common',
    'ts': '1711200703949',
}

# post请求的data数据需要进行编码
data = urllib.parse.urlencode(data).encode('utf-8')

# 请求对象的定制
request = urllib.request.Request(url=url,data=data,headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应数据
content = response.read().decode('utf-8')

import json

obj = json.loads(content)
print(obj)