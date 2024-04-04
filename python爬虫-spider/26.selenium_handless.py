'''
edge浏览器无头浏览(测试如下):
    1.创建 EdgeOptions 对象
    2.设置 WebDriver 的可执行路径
    3.创建 Edge WebDriver 实例
    4.访问百度首页
    5.打印页面标题
    6.等待 2 秒
    7.关闭浏览器

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from time import sleep

# 创建 EdgeOptions 对象
edge_options = Options()
edge_options.add_argument('--headless')
edge_options.add_argument('--disable-gpu')

# 设置 WebDriver 的可执行路径
service = Service('./msedgedriver.exe')

# 创建 Edge WebDriver 实例
bro = webdriver.Edge(service=service, options=edge_options)

# 访问百度首页
bro.get('https://www.baidu.com')

# 打印页面标题
print(bro.title)

# 等待 2 秒
sleep(2)

# 关闭浏览器
bro.quit()
'''



# 封装使用

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from time import sleep


def edge_handless():
    # 创建 EdgeOptions 对象
    edge_options = Options()
    edge_options.add_argument('--headless')
    edge_options.add_argument('--disable-gpu')

    # 设置 WebDriver 的可执行路径,注意此处是驱动的路径，并非浏览器路径
    service = Service('./msedgedriver.exe')

    # 创建 Edge WebDriver 实例
    browser = webdriver.Edge(service=service, options=edge_options)
    return browser


browser = edge_handless()

# 访问网页
browser.get('https://chat.openai.com/')

# 打印页面标题
print(browser.title)

# 保存快照
browser.save_screenshot('26.快照测试.png')

# 等待 2 秒
sleep(2)

# 关闭浏览器
browser.quit()
