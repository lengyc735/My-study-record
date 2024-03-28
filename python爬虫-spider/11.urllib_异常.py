
import urllib.request, urllib.error

url = 'https://blog.csdn.net/m0_73367097/article/details/1360272347' # 注：7是自己加的

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
}

try:
    request = urllib.request.Request(url=url, headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    print(content)

except urllib.error.URLError:
    print('请求失败')