"""
爬漫画的：新网球王子 http://www.cartoonmad.com/comic/1079.html
用于实时保存图片地址部分，用数据库实现比较好
"""

import requests
import re
import os
import json


def get_imdict(url):
    data = requests.get(url)
    data.encoding = ('big5')  # 已知网页源码为big5编码
    html = data.text
    categories = zip(re.findall('第(\s[0-9]+\s)話', html),
                     re.findall('([0-9]+)頁', html),
                     re.findall('href=(.*?)target=_blank>第', html))
    imdict = {}
    option = int(input('你想下载前多少话的？'))
    for i in list(categories)[:option]:  # 要加list：zip对象不可迭代
        imlist = []
        for j in range(int(i[1])):
            j += 1
            pageurl = "http://www.cartoonmad.com" + \
                      i[2][:-7] + str(j) + '.html'
            pagedata = requests.get(pageurl)
            pagedata.encoding = 'big5'
            pagehtml = pagedata.text
            imurl = re.findall('src="(http://web4.*?\.jpg)', pagehtml)[0]
            print(imurl)
            imlist.append(imurl)
        print('第%s回合图片地址下载完成' % i[0])
        imdict[i[0]] = imlist
        # 进行文件读写，实现实时保存
        with open('网球王子漫画URL.json', 'w') as f:
            f.write('')
            json.dump(imdict, f)
        print('第%s回合图片地址保存完成' % i[0])

    print('所有图片地址下载保存完成！')
    return imdict


def get_images(imlist):
    index = 1
    for imurl in imlist:
        print('downloading image%s...' % index)
        filename = str(index) + '.jpg'
        img = requests.get(imurl).content
        with open(filename, 'wb') as f:
            f.write(img)
        index += 1


def main():
    try:
        os.mkdir('d://Desktop/网球王子漫画下载')
    except:
        pass
    os.chdir('d://Desktop/网球王子漫画下载')

    url = "http://www.cartoonmad.com/comic/1079.html"
    imdict = get_imdict(url)
    for i in imdict.keys():
        os.mkdir(i)
        os.chdir(i)
        print('第%s回漫画开始下载' % i)
        get_images(imdict[i])
        print('第%s回漫画下载完毕' % i)
        os.chdir('..')


main()
