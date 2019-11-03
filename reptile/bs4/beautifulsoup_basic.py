from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


html = urlopen("https://morvanzhou.github.io/static/scraping/table.html")
soup = BeautifulSoup(html, "lxml")
# 匹配任何形式链接，在.jpg结尾
# img_links = soup.find_all('img', {'src': re.compile('.*?\.jpg')})
# for link in img_links:
#     print(link['src'])
course_links = soup.find_all(
    'a', {'href': re.compile("https://morvan.*")}
)
for link1 in course_links:
    print(link1['href'])
