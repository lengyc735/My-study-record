

# 测试环境 edge浏览器
# from selenium import webdriver
# from time import sleep
# browser = webdriver.Edge()
# browser.get('https://www.huya.com')
# sleep(2)
# browser.close()


from selenium import webdriver
import time 
from selenium.webdriver.common.by import By

browser = webdriver.Edge()

url = 'https://www.baidu.com/'
browser.get(url)

# 打开淘宝
# browser.get('https://www.taobao.com')
# time.sleep(3)

# 后退到(返回)百度页面
# browser.back()
# time.sleep(3)

# 前进的淘宝页面
# browser.forward()
# time.sleep(3)

# 刷新页面
# browser.refresh()


# button = browser.find_element_by_id('su')
# print(button)

# 网页标题
#print()   # 换行方便看
#print(browser.title)

# 当前网址
#print(browser.current_url)

# 浏览器名称
#print(browser.name)

# 网页源码
#print(browser.page_source)


time.sleep(2)
value = browser.find_element(by=By.ID, value='su')

# 获取标签属性
print('\n', value.get_attribute('class'))
# 获取标签名字
print(value.tag_name)

# 获取元素文本
a = browser.find_element(By.LINK_TEXT,'新闻')
print(a.text,'\n')

browser.quit()