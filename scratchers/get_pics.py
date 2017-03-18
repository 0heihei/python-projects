#encoding-utf8
import urllib.request
import socket
import re

socket.setdefaulttimeout(8)
headers = {}
headers['Connection'] = 'Keep-Alive'
headers['Accept-Language'] = 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans'
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
def get_url():
	url=input("Please enter the url:")
	return url
def get_html(url):
	req=urllib.request.Request(url,headers=headers)
	data = urllib.request.urlopen(req).read()
	data = data.decode('utf8')
	return data
def getImage(data):
	imList = re.findall(r'="https?:\S*?\.png|="https?:\S*?\.jpg', data)  # 此处正则用得很不好
	for i in range(len(imList)):
		imList[i] = imList[i].replace('="', '')
	print('downloading...')
	name = 1
	for imgurl in imList:
		print('downloading image%s...'%name)
		urllib.request.urlretrieve(imgurl, r'images/%s.jpg' % name)
		name += 1
	print('Got', len(imList), 'images!')
def main():
	url=get_url()
	data=get_html(url)
	getImage(data)

main()