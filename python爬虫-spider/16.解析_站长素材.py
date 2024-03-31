import urllib.request
from lxml import etree


# 分析
# 第一页：https://sc.chinaz.com/tupian/dongman.html
# 第二页：https://sc.chinaz.com/tupian/dongman_2.html
# 第三页：https://sc.chinaz.com/tupian/dongman_3.html


def create_request(page):
    '''请求对象的定制'''
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/dongman.html'
    else:
        url = 'https://sc.chinaz.com/tupian/dongman_%d.html' % page

    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
    }
    request = urllib.request.Request(url=url,headers=headers)
    return request


def get_content(request):
    '''发送请求'''
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(content):
    '''解析数据 下载'''
    tree = etree.HTML(content)

    name_list = tree.xpath('//div[@data-marginr="16"]/div/img/@alt')
    # print(len(name_list))
    # for name in name_list:
    #     print(name)

    src_list = tree.xpath('//div[@data-marginr="16"]/div/img/@data-original')
    # 如果图片懒加载
    # src_list = tree.xpath('//div[@data-marginr="16"]/div/img/@src2')
    for i in range(len(src_list)):
        name = name_list[i]
        src = src_list[i]
        url = 'https:' + src
        filename = r"D:\MyGit\My-study-record\python爬虫-spider\16.img下载\\" + name + '.jpg'
        #print(name,url)

        #下载图片
        try:
            urllib.request.urlretrieve(url,filename = filename)
        except urllib.error.URLError as e:
            print(f'Error download image {name}: {e}')


if __name__ == '__main__':
    str_page = int(input('请输入要爬取的第一页页数：'))
    end_page = int(input('请输入结束页数：'))

    for page in range(str_page,end_page+1):
        # 请求对象的定制
        request = create_request(page)
        # 获取源码
        content = get_content(request)
        # 解析数据 下载
        down_load(content)
