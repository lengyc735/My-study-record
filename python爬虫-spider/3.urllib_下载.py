import urllib.request

# 下载网页
url_page = 'http://www.baidu.com'

# url代表下载路径，filename代表文件名
urllib.request.urlretrieve(url_page, '3_baidu.html')


# 下载图片
url_imag = 'https://th.bing.com/th/id/OIP.3xyzYqzwuvj13svM4mwyIgHaHa?w=181&h=181&c=7&r=0&o=5&dpr=1.5&pid=1.7'

urllib.request.urlretrieve(url = url_imag, filename = '3_imag.jpg')

# 下载视频
url_video = 'https://v.qq.com/txp/iframe/player.html?vid=v3516tlgh59&tiny=0&auto=1&mute=0'

urllib.request.urlretrieve(url_video,'3_video.mp4')