from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random

url_basic = "https://baike.baidu.com"
his = ["/item/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F/1700215"]

# 需要爬几次
for i in range(20):
    # 合并成实际的url
    url = url_basic + his[-1]
    # 打开，爬取，转成utf-8
    html = urlopen(url).read().decode("utf-8")
    # 添加到，soup ，并选择解析器
    soup = BeautifulSoup(html, features='lxml')
    # 输出结果，标题和url的形式
    print(i, soup.find('h1').get_text(), 'url:', his[-1])
    # 在爬取第二层
    soup_url = soup.find_all("a",
                  {"target": "_blank",
                   "href": re.compile("/item/(%.{2})+$")
                   })
    # 如果爬取到不等于了，就随机在那个网页找一个关键词，继续爬
    if len(soup_url) != 0:
        his.append(random.sample(soup_url, 1)[0]['href'])
    else:
        # 找不到有效的子链接,就删除
        his.pop()
