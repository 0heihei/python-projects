# encoding=utf8
""" 
	爬取一天世界   https://blog.yitianshijie.net/  博文的简易爬虫实现
	请预先建立  readLog.txt  文件
	Requirements:
	requests
	lxml
	bs4
"""

import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time, sys

# 使用BeautifulSoup解析HTML
def analyse(node):
	blogTitle = node.a.string
	blogUrl = node.a['href']
	blogTime = node.span.time['datetime'][0:10]
	blogAuthor = node.span.find_next_sibling('span').span.string
	blogBody = ''
	for string in node.find('div', attrs={'class': 'entry-content'}).strings:
		blogBody += string
	blog = '『%s』\n\n by %s  %s \n%s \n%s ' % (blogTitle, blogAuthor, blogTime, blogBody, blogUrl)
	return blog


def send2email(blog):
	try:
		msg = MIMEText(blog, 'plain', 'utf-8')  # 纯文本邮件
		subject = '【一天世界】博文更新'
		sender = 'cloud_sophier@163.com'
		password = 'd19960808'
		receiver = 'd15821917291@gmail.com'
		smtp_server = 'smtp.163.com'

		msg['Subject'] = Header(subject, 'utf-8')
		msg['From'] = 'cloud_sophier@163.com'
		msg['To'] = 'd15821917291@gmail.com'

		server = smtplib.SMTP_SSL(smtp_server, 99)
		server.set_debuglevel(0)
		server.login(sender, password)
		server.sendmail(sender, [receiver], msg.as_string())
		server.quit()
		return 1
	except Exception as e:
		print(e)
		return 0

def Push():
	headers = {}
	headers['Connection'] = 'Keep-Alive'
	headers['Accept-Language'] = 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans'
	headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'

	url = 'https://blog.yitianshijie.net/'
	res = requests.get(url, headers=headers, verify=False)
	soup = BeautifulSoup(res.text, 'lxml')
	content = soup.find_all('article', limit=5)
	with open('readLog.txt', 'r+') as f:
		ids = f.readlines()
		for node in content:
			if not (node['id'] + '\n') in ids:
				blog = analyse(node)
				if not send2email(blog) ==0:
					f.write(node['id'] + '\n')
					print('-------------------Successful!--------------------')
				else:
					print('----------------------Failed----------------------')
			else:
				print('------------------No new blogs!------------------')

if len(sys.argv) == 1:
	timer = 3600
elif len(sys.argv) == 2:
	if sys.argv[1] == "-q":
		sys.exit()
	if sys.argv[1] == "-t":
		print('参数格式错误')
		sys.exit()
	else:
		if sys.argv[1] == "-h":
			print('''
Run:	$python blogCrawler.py
Options:
	-q:退出
	-h:帮助
	-t:检查博文更新的时间间隔(默认为3600s)
BTW:	ctrl+C 终止程序
	请自行进入程序更改邮件相关选项
				 ''')
		sys.exit()
else:
	if sys.argv[1] == "-t":
		try:
			timer=eval(sys.argv[2])
		except:
			print('参数格式错误')
			sys.exit()
	else:
		timer = 3600
while True:
	Push()
	time.sleep(timer)
