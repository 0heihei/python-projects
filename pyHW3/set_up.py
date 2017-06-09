# encoding=utf-8
from login import Login
from app import MyApp

wel_page = Login()
# 没有注册登录则避免显示软件主界面
try:
	if wel_page.state == True:
		main_page = MyApp(wel_page)
except AttributeError:
	pass
