# encoding=utf8
import urllib.request
import json

url = 'http://news.cctv.com/data/index.json'

res = urllib.request.urlopen(url).read()
lis = json.loads(res)['rollData']
for i in lis:
	print ('标题:%s\n概要:%s\nurl:%s\n时间:%s\n\n' % ( i['title'], i['description'], i['url'], i['dateTime']))