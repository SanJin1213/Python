# 导入需要使用的包，requests获取页面，beautifulsoup解析页面
import requests
from bs4 import BeautifulSoup
import pickle

# url是爬取的目标地址，path是需要保存的本地路径
url = 'https://car.autohome.com.cn/photo/series/37472/1/4708264.html#pvareaid=2042264'
path = 'd:/TOFU/Github/github_learn/VSCode_git_github/Python/reptile/images/'
res = requests.get(url)
res.encoding = 'gb2312'
html = res.text
# print(html)

# # 解析获取到的数据
soup = BeautifulSoup(html, "html.parser")
# print(soup)
class_list = soup.find('div', class_='pic')
print(class_list)
# li_list = class_list.find_all('img',id_='img')
# # print(li_list)

# 循环li，将每一个li都爬取下来
for cla in class_list:
    img = class_list.find('img')
    # print(img)
    img_src = 'http://' 
    # print(img_src)
# # with open(path, "wb") as fp:
#     fp.write(img)
# # 将取到的链接img_src一一访问，获取图片内容，保存到本地
data = requests.get(img_src, stream=True).content
with open(path + '/' + img_src.split('/')[-1], 'wb') as fp:
    fp.write(data)
