import requests
import http.cookiejar
import zlib, json
import urllib.parse
import os
import re

# 开始构造表单
s = requests.Session()
html = s.get('http://electsys.sjtu.edu.cn/edu/login.aspx').content.decode('utf8')
sid = re.findall('name="sid" value="(.+?)"', html)[0]
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
post_data = {
	'sid': sid,
	'returl': returl,
	'v': '',
	'user': usr,
	'pass': pwd,
	'captcha': captcha
}
post_data=urllib.parse.urlencode(post_data).encode('utf8')

url = 'https://jaccount.sjtu.edu.cn/jaccount/ulogin'

req = s.post(url, data=post_data,)

url2='http://electsys.sjtu.edu.cn/edu/student/elect/electwarning.aspx?xklc=1'
post_data2 = {
	'__VIEWSTATE': '/wEPDwUKLTQzMTk1OTAyMg8WAh4EeGtsYwUBMWQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFCUNoZWNrQm94MWNhFMcb/llVDn1pEFCfZhKhz0Iu',
	'__VIEWSTATEGENERATOR': '3E0056E4',
	'__EVENTVALIDATION': '/wEWAwLo2+nsBgKC5Ne7CQKYm8bUB30QDdUU0pi5HAxqqqHPwRKssl/e',
	'CheckBox1': 'on',
	'btnContinue': '继续'
}
post_data2=urllib.parse.urlencode(post_data2).encode('utf8')
req=s.post(url2,post_data2)
print(req.content.decode('utf8'))
