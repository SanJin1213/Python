# post 的使用类型
# 账户登陆
# 上传图片
# 搜索内容
# 上传文件
# 往服务器传数据等

# get 的使用类型
# 正常打开网页
# 不往服务器传数据等

import requests
# 查找关键字
# import webbrowser
# param = {"wd": "莫烦Python"}
# r = requests.get('http://www.baidu.com/s', params=param)
# print(r.url)
# webbrowser.open(r.url)

# 上传图片
# file = {'uploadFile': open('./image.png', 'rb')}
# r = requests.post('http://pythonscraping.com/pages/files/processing2.php', files=file)
# print(r.text)

# 登陆页面，并返回信息
# data = {'firstname': 'wangx', 'lastname': 'in'}
# # 登陆网页，然后将数据提交上去，
# r = requests.post('http://pythonscraping.com/pages/files/processing.php', data=data)
# print(r.text)

#  普通提交和获取页面信息
# payload = {'username': 'Morvan', 'password': 'password'}
# r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php',
#                   data=payload)
# print(r.cookies.get_dict())
# r = requests.get('http://pythonscraping.com/pages/cookies/profile.php',
#                  cookies=r.cookies)
# print(r.text)

# 先搭建一个session，在提交获取页面信息
session = requests.Session()
payload = {'username': 'Morvan', 'password': 'password'}
# 用session 提交 data这种的个人信息
r = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
# 用字典的形式 输出刚才提交的内容，二次查看
print(r.cookies.get_dict())
# 直接用session 获取刚才登陆成功页面的信息
r = session.get("http://pythonscraping.com/pages/cookies/profile.php")
print(r.text)
