import requests
import os
from bs4 import BeautifulSoup
import bs4


def get_pages(page_num):
    # get 20 pages
    # for i in range(1, page_num+1):
    #     page_url = 'https://price.pcauto.com.cn/cars/sg10891-o1-' + str(i) + '/'
    #     get_html(page_url)
    page_url = 'https://price.pcauto.com.cn/cars/sg10891-o1-2/'


def get_html(page_url):
    # get page's html
    result_page = requests.get(page_url)
    page_html = BeautifulSoup(result_page.text, "html.parser")
    # get pic html
    photo_list = page_html.find('div', class_='imgWrap')
    if isinstance(photo_list,bs4.element.Tag):  
        img_lists = photo_list.find('img')
        print(img_lists)
        # cnt = 0
        # for img_list in img_lists:
        #     if cnt % 3 == 1:
        #         img_tag = img_list.img
        #         img_src = img_tag.get("src")
        #         # img_width = img_tag.get("width")
        #         # img_height = img_tag.get("height")
        #         # img_name = str(img_width) + "x" + str(img_height)
        #         img_url = 'http:' + img_src
        #         img_urls.append(img_url)
        #         img_names.append(img_name)
        #     cnt += 1
        img_urls = "http:/img.pcauto.com.cn/images/upload/upc/tx/auto5/1808/24/c9/105161523_1535073687001_270x202.jpg"

def get_picture(img_urls, img_names):
    # get pictures using img_url
    for i in range(0, len(img_urls)):
        pic = requests.get(img_urls[i])
        # with open(localPath + 'livingroom_' + img_names[i] + '_' + str(i) + '.jpg', 'wb') as f:
        #     f.write(pic.content)
        with open(localPath,'wb') as f:
            f.write(pic)


# def save_picture():
    # save picture with size

# page_num = 20
# img_urls = []
# img_names = []
# print(img_urls)
localPath = 'd:\TOFU/'
# if not os.path.exists(localPath):
#     os.mkdir(localPath)
# get_pages(page_num)
# get_picture(img_urls, img_names)
