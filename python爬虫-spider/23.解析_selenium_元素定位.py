
# 测试环境：Edge浏览器

# from selenium import webdriver
# from time import sleep 
# browser = webdriver.Edge()
# browser.get(r'https://www.baidu.com/')
# sleep(7)
# browser.close()


from selenium import webdriver
import time
from selenium.webdriver.common.by import By


browser = webdriver.Edge()

#browser.maximize_window()   # 设置浏览器全屏
url = 'https://www.baidu.com/'
browser.get(url)
time.sleep(3)



'''
属性
函数
  1---------------

CLASS
find_element(by=By.CLASS_NAME, value='')

  2---------------

XPATCH
find_element(by=By.XPATH, value='')

  3---------------

LINK_TEXT
find_element(by=By.LINK_TEXT, value='')

  4----------------

PARTIAL_LINK_TEXT
find_element(by=By.PARTIAL_LINK_TEXT, value='')

  5----------------

NAME
find_element(by=By.NAME, value='')

  6----------------

TAG
find_element(by=By.TAG_NAME, value='')

  7----------------

CSS
find_element(by=By.CSS_SELECTOR, value='')

  8-----------------

ID
find_element(by=By.ID, value='')
'''

# 根据标签属性查找元素
# element = browser.find_element(By.ID, 'su')
# print(element)

# 根据xpath语句来获取对象
# button = browser.find_element(By.XPATH, '//input[@id="su"]')
# print(button)

# 根据标签的名字来获取对象
# button = browser.find_element(By.TAG_NAME, 'input')
# print(button)
 
# 使用bs4的语法老获取对象
# button = browser.find_element(By.CSS_SELECTOR, 'input#su')
# print(button)

# 获取链接文本
# button = browser.find_element(By.LINK_TEXT, '新闻')
# print(button)


# 关闭浏览器
# time.sleep(3)
# browser.close()