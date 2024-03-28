# url

# 第一页
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&
# start=0&limit=20

# 第二页
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=20&limit=20

# 第三页
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=40&limit=20

# 对比可发现 stare= 后参数不一样 limit=20 为每页显示的数量


# 1.请求对象定制
# 2.发送请求
# 3.下载数据

import urllib.parse, urllib.request

def create_request(page):
    '''每一页对象定制'''
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
    
    data = {
        'start':(page-1)*20,
        'limit':20
    }

    data = urllib.parse.urlencode(data)

    url = base_url + data

    print(f'{url}的内容已下载')

    headers = {
         'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
    }

    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    '''获取响应数据'''
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(content):
    with open('10.douban.json','w',encoding='utf-8') as fi:
        fi.write(content)

# 程序入口
if __name__ == '__main__':
    start_page = int(input('请输入起始页:'))
    end_page = int(input('请输入终止页:'))

    for page in range(start_page, end_page+1):
        request = create_request(page)
        content = get_content(request)
        down_load(content)