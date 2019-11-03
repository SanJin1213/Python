# BeautigulSouo 的学习教程

## 一、导入
    pip install bs4

## 二、导入引用

```python
from bs4 import BeautifulSoup
```

### 三、基本操作

#### 1. 查找，find和fina_all，高级选择

```python
from bs4 import BeautifulSoup
from urllib.request import urlopen


html = "要爬取的网页的网址"
soup = BeautifulSoup(html)
jan = soup.find('ul', {"class":"jan"})
# 类似于正则表达式，先匹配所有的ul
# 在匹配完所有的ul之后再匹配class=jan 的target
d_jan = jan.find_all('li')
# 在搜索完jan的条件后，在查找所有target=li 的数据
for d in d.jan:
    print(d.get_text)
    # d.get_text 是d中的信息，以文本的形式输出
```

#### 2. 解析网页：正则表达式

#### 3. 爬取百度百科

[爬取百度百科](bs4_baidubaike.py)

1. 首先我们需要爬取的网页信息进行拆分，分成百度的基础网址和会更改的网址
（这样分的优势是，为了方便以后再次爬取相同类型的页面信息）

2. 