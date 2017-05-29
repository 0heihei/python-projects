import requests
import http.cookiejar
import zlib, json
import urllib.parse
import os,re
from bs4 import BeautifulSoup

headers = {
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,ja;q=0.2,zh-TW;q=0.2',
		'Connection': 'keep-alive',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
	}
s = requests.Session()
s.headers=headers
req = s.get('http://electsys.sjtu.edu.cn/edu/')
cookies_dict = {
	'ASP.NET_SessionId': req.cookies['ASP.NET_SessionId'],
	'mail_test_cookie': req.cookies['mail_test_cookie']}
cookies = requests.utils.cookiejar_from_dict(cookies_dict)

def login():
	req=s.get('http://electsys.sjtu.edu.cn/edu/login.aspx',allow_redirects=False)
	req2=s.get(req.headers['Location'],allow_redirects=False)
	req3=s.get(req2.headers['Location'])
	html = req3.content.decode('utf8')
	sid = re.findall('name="sid" value="(.+?)"', html)[0]  # 有待用美丽汤改写
	returl = re.findall('name="returl" value="(.+?)"', html)[0]
	se = re.findall('name="se" value="(.+?)"', html)[0]
	# usr=input('请输入用户名：')
	# pwd=input('请输入密码：')
	usr = 'duanyunzhi'
	pwd = 'sjtu184052'
	vfcode = s.get('https://jaccount.sjtu.edu.cn/jaccount/captcha').content
	with open('vf_code.png', 'wb') as f:
		f.write(vfcode)
	os.startfile("vf_code.png")
	captcha = input("输入验证码：")
	#构造表单
	login_data = {
		'sid': sid,
		'returl': returl,
		'v': '',
		'user': usr,
		'pass': pwd,
		'captcha': captcha
	}
	login_data = urllib.parse.urlencode(login_data).encode('utf8')
	# 登录
	login_url = 'https://jaccount.sjtu.edu.cn/jaccount/ulogin'
	login = s.post(login_url, data=login_data,allow_redirects=False)
	print(login.headers)

login()


'''
post_url = 'http://electsys.sjtu.edu.cn/edu/student/elect/electwarning.aspx?xklc=1'
post_data = {
	'__VIEWSTATE': '/wEPDwUKLTQzMTk1OTAyMg8WAh4EeGtsYwUBMWQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFCUNoZWNrQm94MWNhFMcb/llVDn1pEFCfZhKhz0Iu',
	'__VIEWSTATEGENERATOR': '3E0056E4',
	'__EVENTVALIDATION': '/wEWAwLo2+nsBgKC5Ne7CQKYm8bUB30QDdUU0pi5HAxqqqHPwRKssl/e',
	'CheckBox1': 'on',
	'btnContinue': '继续'
}
post_data = urllib.parse.urlencode(post_data).encode('utf8')
#此处必须要更新cookies，不然通不过验证

cookies = requests.utils.cookiejar_from_dict(cookies_dict)
s.cookies = cookies   #因为cookie的原因，必须保持网页端登录状态这里才可以登录？
get_courses = s.post(post_url, post_data)

html=s.get('http://electsys.sjtu.edu.cn/edu/student/elect/speltyRequiredCourse.aspx').content.decode('utf8')
soup=BeautifulSoup(html,'lxml')
course_list=[ i for i in soup.find_all('table',id="SpeltyRequiredCourse1_gridMain")[0]]
print('Your courses:')
for i in course_list[2:-2]:
	print(i.find_all('td')[2].string,i.find_all('td')[1].string)
course_code=input('输入你要查看的课程的代码：')
course_code=course_code.upper()
data={
	'__VIEWSTATE':soup.find_all('input',id='__VIEWSTATE')[0]['value'],
	'__VIEWSTATEGENERATOR':soup.find_all('input',id='__VIEWSTATEGENERATOR')[0]['value'],
	'__EVENTVALIDATION':soup.find_all('input',id='__EVENTVALIDATION')[0]['value'],
	'myradiogroup':course_code,
	'SpeltyRequiredCourse1$lessonArrange':'课程安排'
}
data=urllib.parse.urlencode(data).encode('utf8')
post=s.post('http://electsys.sjtu.edu.cn/edu/student/elect/speltyRequiredCourse.aspx',data)  #提交查看该课程
print(post.headers)  #获取response的headers中的location，凭此get到该课程的地址
'''