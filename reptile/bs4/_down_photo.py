from bs4 import BeautifulSoup
import requests
import os


URL = "http://www.ngchina.com.cn/animals/"

# 查找图片列表
# 获取url
html = requests.get(URL).text
soup = BeautifulSoup(html, features='lxml')
# 筛选
img_ul = soup.find_all('ul', {"class": "img_list"})
print(len(img_ul))

# # 存放文件(如果想存在已经建好的文件夹里，请忽略)
# file_location = "d:/TOFU/Github/github_learn/VSCode_git_github/Python/reptile/bs4/images/"
# # os.makedirs(file_location, exist_ok=True)

# # 遍历img_ul
# for ul in img_ul:
#     # 找出ul下所有的img标签
#     imgs = ul.find_all("img")
#     for img in imgs:
#         # 提取img中的src
#         url = img['src']
#         # 获取照片
#         r = requests.get(url, stream=True)
#         image_name = url.split('/')[-1]
#         print(image_name)
#         with open(file_location + '%s' % image_name, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=128):
#                 f.write(chunk)
#         print("Saved %s" % image_name)
