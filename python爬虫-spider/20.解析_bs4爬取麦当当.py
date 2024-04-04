
import urllib.request

url = 'https://www.mcdonalds.com.cn/product/mcdonalds/hamburgers'

response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')

# print(content)

from bs4 import BeautifulSoup

soup = BeautifulSoup(content,'lxml')

# //span[@class="name"]
name_list = soup.select('span.name')

for name in name_list:
    #print(name.string)
    print(name.get_text())