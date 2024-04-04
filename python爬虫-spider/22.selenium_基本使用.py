
# 测试edge浏览器驱动是否安装
# from time import sleep
# from selenium import webdriver
 
# driver = webdriver.Edge()
 
# driver.get(r'https://www.baidu.com/')
 
# sleep(5)
# driver.close()



# 导入
from selenium import webdriver

# 1.创建浏览器操作对象

#path = 'MicrosoftWebDriver.exe'

browser = webdriver.Edge()

# 2.访问网站
# url = 'https://www.baidu.com/'
# browser.get(url)

url = 'https://miaosha.jd.com/'

browser.get(url)

# 3.获取网页源码
# page_source获取源码
content = browser.page_source
print(content)