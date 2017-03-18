# encoding=utf8
"""
    爬取一天世界   https://blog.yitianshijie.net/  博文的简易爬虫实现
	请先在相同目录下建立  readLog.txt  文件
	requirements:
	requests
	lxml
	bs4
	这个oop版本需要很大改进。。。
"""
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time, sys

class blogCrawler:
	def __init__(self):
		pass

	def analyse(self,node):
		self.blogTitle=node.a.string
		self.blogUrl=node.a['href']
		self.blogTime = node.span.time['datetime'][0:10]
		self.blogAuthor = node.span.find_next_sibling('span').span.string
		self.blogBody = ''
		for string in node.find('div', attrs={'class': 'entry-content'}).strings:
			self.blogBody += string
		self.blog = '『%s』\n\n by %s  %s \n%s \n%s ' % (self.blogTitle, self.blogAuthor, self.blogTime, self.blogBody, self.blogUrl)
		return self.blog

	def send2email(self,blog):
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

			server = smtplib.SMTP(smtp_server, 25)
			server.set_debuglevel(1)
			server.login(sender, password)
			server.sendmail(sender, [receiver], msg.as_string())
			server.quit()
			return 1
		except:
			return 0

	def Push(self):
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
					blog = self.analyse(node)
					if not self.send2email(blog) == 0:
						f.write(node['id'] + '\n')
						print('-------------------Successful!--------------------')
					else:
						print('---------------Error: send2email()---------------')
				else:
					print('------------------No new blogs!------------------')

	def start(self):
		mark1=1
		mark2=1
		self.timer=1
		while 1:
			if mark1==1:
				self.Push()
				time.sleep(self.timer)
			if mark2==1:
				cmd = input("Options:")
				if cmd == "-q":
					break
				elif cmd == "-h":
					print('''
								Run:	$python blogCrawler.py
								Options:
									-q:退出
									-h:帮助
									-t:检查博文更新的时间间隔(默认为3600s)
								BTW:	ctrl+C 终止程序
									请自行进入程序更改邮件相关选项
												 ''')
					mark1 = 0
				elif len(cmd.split()) == 2:
					try:
						self.timer = eval(cmd.split()[1])
						mark2=0
					except:
						pass
				else:
					print("输入错误")
					mark1 = 0

crawler=blogCrawler()
crawler.start()
