from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random


base_url = "https://baike.baidu.com"
# 这里类似乱码的是 中文不显示，只能用这样的方式显示中文
# his  是用来收集之前爬到过的选择过的网页，反复爬取

# his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]
# # 从his 抽取最后一个在和base_url合并形成新的url
# url = base_url + his[-1]

# # 用urlopen读取数据，解析成utf-8
# html = urlopen(url).read().decode('utf-8')
# # 放到soup里面，将解析器，设置为lxml
# soup = BeautifulSoup(html, features='lxml')
# # 将爬取到的h1标题，用文本的形式输出，一直匹配到 his 的最后一个元素
# # 找到h1的这个target，显示网页爬虫信息，输出url为
# # find 找到第一个，然后返回
# print(soup.find('h1').get_text(), '    url: ', his[-1])

# # find valid urls
# # 正则表达式的解读：
# # find_all 寻找所有的匹配
# # :代表=，/item/ 开头，后面的子表达式（%除换行的两个字符）出现0次或多次，一直匹配到结尾
# sub_urls = soup.find_all(
#     "a", {"target": "_blank", "href": re.compile("/item/(%.{2})+$")})
# print(sub_urls)

# # 如果匹配到的sub_url 只要不等于0，就在sub_url中随机抽取一个target,href 选择出链接
# if len(sub_urls) != 0:
#     his.append(random.sample(sub_urls, 1)[0]['href'])
# else:
#     # no valid sub link found
#     # 重新返回上一个his 然后继续往下爬
#     his.pop()
# print(his)
his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]

for i in range(20):
    url = base_url + his[-1]
    print(url)
    url1 = base_url + his[]
    print(url1)

    # html = urlopen(url).read().decode('utf-8')
    # soup = BeautifulSoup(html, features='lxml')
    # print(i, soup.find('h1').get_text(), '    url: ', his[-1])

    # # find valid urls
    # sub_urls = soup.find_all(
    #     "a", {"target": "_blank", "href": re.compile("/item/(%.{2})+$")})

    # if len(sub_urls) != 0:
    #     his.append(random.sample(sub_urls, 1)[0]['href'])
    # else:
    #     # no valid sub link found
    #     his.pop()
