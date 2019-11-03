# 下载图片
import os
# 这里要看一下终端输出的位置，如果没有会自动新建的
# os.makedirs('.d:/TOFU/Github/github_learn/' +
#             'VSCode_git_github/Python/reptile/bs4/images', exist_ok=True)

IMAGE_URL = ("https://morvanzhou.github.io/" +
            "static/img/description/learning_step_flowchart.png")

# # 方法1 urlretrieve
# from urllib.request import urlretrieve
# # 下载的网址，下载完存放的位置
# urlretrieve(IMAGE_URL, "d:/TOFU/Github/github_learn/VSCode_git_github/Python/reptile/bs4/images/1.png")

# 方法2 使用requests.get
import requests
# # 解读，先获取下载图片的url
# r = requests.get(IMAGE_URL)
# # 读写文件，文件的位置和名字，权限，
# with open("d:/TOFU/Github/github_learn/VSCode_git_github/Python/reptile/bs4/images/2.png",
#           "wb") as f:
#     # text 是 unicode型 的方式写入
#     # 文件写入，以2进制型的写入
#     f.write(r.content)

# 以上两种办法都是，先从网上下载到内存，全部下载好之后在从内存存到本地设定文件位置
# 对于大型的数据，下载，很费时

# 方法3 下了多少就写到本地多少，边下载边存储
# stream 参数要设置成ture
r = requests.get(IMAGE_URL, stream=True)
with open("d:/TOFU/Github/github_learn/VSCode_git_github/Python/reptile/bs4/images/3.png",
          "wb") as f:
    # chunk_size 每次写入文件的单位，bytes
    # r.iter_content 不断以这样的单位重复写入，每次32b，32b
    for chunk in r.iter_content(chunk_size=32):
        # 每次写入chunk
        f.write(chunk)
