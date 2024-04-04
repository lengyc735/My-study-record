 
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Edge()

url = 'https://www.baidu.com/'
browser.get(url)

time.sleep(1)

# 获取文本框信息
input = browser.find_element(By.ID,'kw')

# 在文本框输入信息
input.send_keys('python')

time.sleep(1)

# 获取百度一下按钮
button = browser.find_element(By.ID,'su')

# 点击按钮
button.click()

time.sleep(2)

# 滑到底部
js_bottom = 'document.documentElement.scrollTop=10000'
browser.execute_script(js_bottom)

time.sleep(2)

# 获取下一页按钮
next = browser.find_element(By.XPATH,"//a[@class='n']")
next.click()

time.sleep(2)

# 回到上一页
browser.back()
time.sleep(1)

# 刷新
browser.refresh()
time.sleep(1)

# 前进到下一页
browser.forward()
time.sleep(2)

# 退出
browser.quit()


# 模拟鼠标操作
'''
带入ActionChains类
from selenium.webdriver.common.action_chains import ActionChains


操作     函数
-------------------
右击	context_click()
双击	double_click()
拖拽	double_and_drop()
悬停	move_to_element()
执行	perform()
'''

# 模拟键盘操作
'''
引入Keys类
from selenium.webdriver.common.keys import Keys
---------------
操作	函数
---------------
删除键	send_keys(Keys.BACK_SPACE)
空格键	send_keys(Keys.SPACE)
制表键	send_keys(Keys.TAB)
回退键	send_keys(Keys.ESCAPE)
回车	send_keys(Keys.ENTER)
全选	send_keys(Keys.CONTRL,'a')
复制	send_keys(Keys.CONTRL,'c')
剪切	send_keys(Keys.CONTRL,'x')
粘贴	send_keys(Keys.CONTRL,'x')
键盘F1	send_keys(Keys.F1)
'''


#  cookie操作
# from selenium import webdriver
# browser = webdriver.Chrome()

# 知乎发现页
# browser.get('https://www.zhihu.com/explore')

# 获取cookie
# print(f'Cookies的值：{browser.get_cookies()}')

# 添加cookie
# browser.add_cookie({'name':'才哥', 'value':'帅哥'})
# print(f'添加后Cookies的值：{browser.get_cookies()}')

# 删除cookie
# browser.delete_all_cookies()
# print(f'删除后Cookies的值：{browser.get_cookies()}')
# 总结
