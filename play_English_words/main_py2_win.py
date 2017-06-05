# encoding=utf-8
from Tkinter import *
import tkMessageBox
import tkFileDialog
import tkFont
import urllib
import time
import random
import re
import base64
import json


# 创建 登录界面
class Log:
	def __init__(self):
		self.state = False  # 初始状态为false,即还未登录
		self.r = Tk()
		self.r.title('非常背单词')
		self.r.geometry('300x125')
		self.name = StringVar()
		self.pswd = StringVar()
		self.l1 = Label(self.r, text='账号')
		self.l1.grid(row=3, column=1)
		self.l2 = Label(self.r, text='密码')
		self.l2.grid(row=4, column=1)
		self.e1 = Entry(self.r, textvariable=self.name)
		self.e1.bind('<Return>', self.ok)  # 回车键确认
		self.e1.grid(row=3, column=2)
		self.e2 = Entry(self.r, textvariable=self.pswd, show='*')
		self.e2.bind('<Return>', self.ok)
		self.e2.grid(row=4, column=2)
		self.v1 = IntVar()
		self.v1.set(1)
		self.rb1 = Radiobutton(self.r, text='登录', variable=self.v1, value=1)
		self.rb1.grid(row=1, column=1, padx=30)
		self.rb2 = Radiobutton(self.r, text='注册', variable=self.v1, value=0)
		self.rb2.grid(row=1, column=2, sticky=E)
		self.bt1 = Button(self.r, text='确认', command=self.reg_or_log)
		self.bt1.grid(row=5, column=1)
		self.bt2 = Button(self.r, text='重输', command=self.re_enter)
		self.bt2.grid(row=5, column=2, sticky=E)
		self.r.mainloop()

	# 选择登录还是注册
	def reg_or_log(self):
		self.get_name = self.name.get().strip()
		self.get_pswd = self.pswd.get().strip()
		if self.get_name == '' or self.get_pswd == '':  # 如果用户未输入信息就提示并重新输入
			tkMessageBox.showwarning(self.r, message='请输入账号或密码！')
			self.re_enter()
			return
		elif not re.match('[a-zA-Z0-9]', self.get_pswd):  # 判断密码格式，不符合标准则提示
			tkMessageBox.showwarning(self.r, message='密码必须是字母和数字的组合！')
			self.re_enter()
			return
		else:
			self.f = open('Users/usersInfo.json', 'r')
			self.userDict = json.load(self.f)
			self.f.close()
			# 用户选择注册，加密保存用户信息
			if self.v1.get() == 0:
				if self.get_name in self.userDict:
					tkMessageBox.showerror(message='用户名已存在!')
					self.re_enter()
					return
				else:
					tkMessageBox.showinfo(self.r, message=' 成功注册！')
					self.userDict[self.get_name] = base64.encodestring(self.get_pswd)
					with open('Users/usersInfo.json', 'w') as f:
						json.dump(self.userDict, f)
					self.state = True
			# 用户选择登录，验证用户信息
			elif self.v1.get() == 1:
				if self.get_name in self.userDict:
					if self.userDict[self.get_name] == base64.encodestring(self.get_pswd):
						tkMessageBox.showinfo(self.r, message='成功登录！')
						self.state = True  # 登录状态信号变为true
					else:
						tkMessageBox.showerror(self.r, message='密码错误！')
						self.re_enter()
						return
				else:
					tkMessageBox.showerror(self.r, message='用户名错误！')
					self.re_enter()
					return
			self.r.destroy()

	def re_enter(self):
		"""
		在输入错误的情况下把原先的内容清空以便重新输入
		"""
		self.pswd.set('')
		self.name.set('')

	def ok(self, event):
		"""回车键事件"""
		self.reg_or_log()


# 创建 主程序界面
class MyApp:
	def __init__(self):
		self.root = Tk()
		self.root.minsize(820, 500)
		self.root.title('玩转单词')
		self.ft = tkFont.Font(font=('Microsoft YaHei', 12, 'normal'))
		self.userName = wel_page.get_name
		# 以下菜单部分分为  出题词库、题目形式、附加功能、其他信息
		self.m = Menu(self.root)
		self.root.config(menu=self.m)
		self.m1 = Menu(self.m)  ##### 菜单一
		self.m.add_cascade(label="词库", menu=self.m1)
		self.m1.add_radiobutton(label="四级", command=self.getCET4)
		self.m1.add_radiobutton(label="六级", command=self.getCET6)
		self.m1.add_radiobutton(label="其它", command=self.getOthers)
		self.m2 = Menu(self.m)  ##### 菜单二
		self.m.add_cascade(label="形式", menu=self.m2)
		self.m2.add_radiobutton(label="填空题", command=self.wordCompletion)
		self.m21 = Menu(self.m2)
		self.m2.add_cascade(label='选择题', menu=self.m21)
		self.m21.add_radiobutton(label='英-->汉', command=self.en_to_ch)
		self.m21.add_radiobutton(label='汉-->英', command=self.ch_to_en)
		self.m3 = Menu(self.m)  ##### 菜单三
		self.m.add_cascade(label='功能', menu=self.m3)
		self.m3.add_command(label='增词', command=self.addWords)
		self.m3.add_command(label='查词', command=self.searchWord)
		self.m31 = Menu(self.m3)
		self.m3.add_cascade(label='分析', menu=self.m31)
		self.m31.add_command(label='四级词汇', command=self.analyseCET4)
		self.m31.add_command(label='六级词汇', command=self.analyseCET6)
		self.m4 = Menu(self.m)  ##### 菜单四
		self.m.add_cascade(label="关于", menu=self.m4)
		self.m4.add_command(label='信息', command=self.about)
		self.m4.add_command(label='用户', command=self.usersInfo)
		# 下面的frame用来输出用户答题的判断结果
		self.f2_0 = Frame(self.root, height=125, width=600, bd=4, bg='DarkGray')
		self.f2_0.place(x=0, y=380)
		# 下面的构件主要是 错词展示栏(misWords)和当前时间栏(l2)
		self.count_of_mis = 0  # 错题数量
		self.count_of_qs = 0  # 总题目数
		self.f3 = Frame(self.root, height=500, width=200, bd=4, bg='DimGray')
		self.f3.place(x=600, y=0)
		self.l1 = Label(self.f3, text='   <错词展示栏>    0/0', font=self.ft, fg='yellow', bg='DimGray')
		self.l1.place(x=0, y=0)
		self.misWords = Listbox(self.f3, height=480, width=300, fg='red', bg='SkyBlue')
		for i in range(700):
			self.misWords.insert(1, ' ')
		self.sl = Scrollbar(self.root)
		self.sl.pack(side=RIGHT, fill=Y)
		self.misWords['yscrollcommand'] = self.sl.set
		self.sl['command'] = self.misWords.yview
		self.misWords.place(x=0, y=30)
		# 时间栏
		self.l2 = Label(self.f3, text="", height=2, width=28, bg='#383838', fg='white')
		self.l2.place(x=0, y=460)
		self.update_clock()

		self.root.mainloop()

	def update_clock(self):
		"""
		更新时间
		"""
		now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
		self.l2.configure(text=now)
		self.root.after(1000, self.update_clock)

	# 下面4个函数获取词库单词
	def getFiles(self, name):
		"""
		打开词库文件，读取所有行(每行只有一个单词及其翻译)
		"""
		if name == '':  # 给出文件对话框供用户选择词库
			self.filename = tkFileDialog.askopenfilename(filetypes=[("all files", "*")], initialdir='./Lexicon')
			try:
				self.f1 = open(self.filename, 'r')
				self.lines = self.f1.readlines()
				self.f1.close()
			except:
				tkMessageBox.showerror('Error', '不能打开文件\n' + str(sys.exc_info()[1]))
			if self.filename == ():
				tkMessageBox.showwarning('Warning', "请选择文件!")
				return
			else:
				tkMessageBox.showinfo('Info', '成功打开文件%s'%str(self.filename.encode('utf8')))
		else:
			self.filename = './Lexicon/' + name
			self.f1 = open(self.filename, 'r')
			self.lines = self.f1.readlines()
			self.f1.close()

	def getWords(self):
		"""
		从之前的列表中选单词作为出题单词
		"""
		self.aLine, self.word, self.expre, self.word1, self.word2, self.word3, self.expre1, self.expre2, self.expre3 \
			= '', '', '', '', '', '', '', '', ''
		while '' in [self.aLine, self.word, self.expre, self.word1, self.word2,
					 self.word3, self.expre1, self.expre2, self.expre3]:  # 防止词库文件有有空行
			try:
				self.aLine = self.lines[random.randint(1, len(self.lines))]
				self.word = self.aLine.split()[0].strip()
				self.expre = self.aLine.split()[1].strip()
				self.word1 = self.lines[random.randint(1, len(self.lines))].split()[0].strip()
				self.word2 = self.lines[random.randint(1, len(self.lines))].split()[0].strip()
				self.word3 = self.lines[random.randint(1, len(self.lines))].split()[0].strip()
				self.expre1 = self.lines[random.randint(1, len(self.lines))].split()[1].strip()
				self.expre2 = self.lines[random.randint(1, len(self.lines))].split()[1].strip()
				self.expre3 = self.lines[random.randint(1, len(self.lines))].split()[1].strip()
			except:
				return None  # none信号 可表明用户没有选词库
		return True

	def getCET4(self):
		"""
		指定读取四级词汇
		"""
		self.getFiles('CET_4.txt')

	def getCET6(self):
		"""
		指定读取六级词汇
		"""
		self.getFiles('CET_6.txt')

	def getOthers(self):
		"""
		由用户自己选择词库
		"""
		self.getFiles('')

	# 填空题
	def wordCompletion(self):
		if self.getWords() == None:  # 防止用户未选词库就点击题型
			tkMessageBox.showerror(message='请先选择词库！')
			return
		tkMessageBox.showwarning(title='Tips', message='输完按 回车键 即可判断并切换')

		# 出题
		def ques():
			global v2
			self.getWords()
			f1 = Frame(self.f1_1, bd=4, relief="groove", height=100, width=100)
			f1.place(x=165, y=100)
			Label(f1, text=self.expre, height=3, width=25, font=self.ft).grid()
			v2 = StringVar()
			e = Entry(f1, width=20, bd=2, textvariable=v2)
			e.bind('<Return>', next_one)
			e.grid()
			Label(f1, text=' ').grid()

		# 判断
		def judge():
			f2_1 = Frame(self.root, height=125, width=600, bd=4, bg='DarkGray')
			f2_1.place(x=0, y=380)

			f2 = Frame(f2_1, relief="groove", height=100, width=100)
			f2.place(x=180, y=0)
			if v2.get() == '' or v2.get().strip().lower() != self.word:  # 答错则保存到错词本
				with open('Users/' + self.userName + '_misWords.txt', 'a+') as f:
					item = self.word + '   ' + self.expre + '\n'
					f.write(item)
				wrong_ans = Label(f2, text='回答错误!\n正确答案是 %s\n已为您添加至错词本！' % self.word, width=25, font=self.ft)
				wrong_ans.grid()
				self.misWords.insert(0, item)  # 答错的词显示在"错词展示栏"界面
				self.count_of_mis += 1
			else:
				right_ans = Label(f2, text='回答正确！', width=25, font=1)
				right_ans.grid()
			self.count_of_qs += 1
			ques()
			self.l3 = Label(self.f3, text='   <错词展示栏>    %s/%s' % (str(self.count_of_mis), str(self.count_of_qs)),
							font=self.ft, fg='yellow', bg='DimGray')  # 更新  "错词展示栏"
			self.l3.place(x=0, y=0)

		def next_one(event):
			"""
			判断这一题，显示下一题
			"""
			judge()

		self.f1_1 = Frame(self.root, height=380, width=600, bd=4, bg='PaleGreen')
		self.f1_1.place(x=0, y=0)
		ques()
		self.bt1 = Button(self.f1_1, text='确认', bd=2, width=8, command=judge)
		self.bt1.place(x=265, y=240)

	# 选择题
	def wordChoice(self):
		if self.getWords() == None:  # 防止用户未选词库就点击题型
			tkMessageBox.showerror(message='请先选择词库！')
			return
		tkMessageBox.showwarning(title='Tips', message='对着选项双击左键即可判断并切换')

		# 出题
		def ques():
			global v3, center, rightItem, rightAns
			self.getWords()
			if self.model == 1:  # 英--->汉
				center, rightAns, ops2, ops3, ops4 = self.word, self.expre, self.expre1, self.expre2, self.expre3
			else:  # 汉--->英
				center, rightAns, ops2, ops3, ops4 = self.expre, self.word, self.word1, self.word2, self.word3
			v3 = IntVar()
			ops = [rightAns, ops2, ops3, ops4]
			random.shuffle(ops)  # 打乱顺序
			A, B, C, D = ops
			rightItem = ops.index(rightAns)

			f3 = Frame(self.f1_2, bd=4, relief="groove", height=100, width=100)
			f3.place(x=180, y=80)
			Label(f3, text=center, width=20, font=self.ft, bd=2).grid()
			rb1 = Radiobutton(f3, text=A, variable=v3, value=0, height=1, font=self.ft)
			rb2 = Radiobutton(f3, text=B, variable=v3, value=1, height=1, font=self.ft)
			rb3 = Radiobutton(f3, text=C, variable=v3, value=2, height=1, font=self.ft)
			rb4 = Radiobutton(f3, text=D, variable=v3, value=3, height=1, font=self.ft)
			rb1.bind('<Double-Button-1>', next_one)
			rb2.bind('<Double-Button-1>', next_one)
			rb3.bind('<Double-Button-1>', next_one)
			rb4.bind('<Double-Button-1>', next_one)
			rb1.grid(stick=W)
			rb2.grid(stick=W)
			rb3.grid(stick=W)
			rb4.grid(stick=W)

		# 判断
		def judge():
			f2_2 = Frame(self.root, height=125, width=600, bd=4, bg='DarkGray')
			f2_2.place(x=0, y=380)
			f4 = Frame(f2_2, relief="groove", height=100, width=100)
			f4.place(x=180, y=0)
			if v3.get() == rightItem:
				right_ans = Label(f4, text='回答正确！', width=25, font=self.ft)
				right_ans.grid()
			else:  # 答错则保存到错词本 "
				with open('Users/' + self.userName + '_misWords.txt', 'a+') as f:
					if self.model == 1:
						item = center + '   ' + rightAns + '\n'
					else:
						item = rightAns + '   ' + center + '\n'
					f.write(item)
				wrong_ans = Label(f4, text='回答错误!\n正确答案是  %s\n已为您添加至错词本！' % rightAns, width=30, font=self.ft)
				wrong_ans.grid()
				self.misWords.insert(0, item)
				self.count_of_mis += 1
			ques()
			self.count_of_qs += 1
			self.l4 = Label(self.f3, text='   <错词展示栏>    %s/%s' % (str(self.count_of_mis), str(self.count_of_qs)),
							font=self.ft, fg='yellow', bg='DimGray')  # 更新 "错词展示栏"
			self.l4.place(x=0, y=0)

		def next_one(event):
			"""
			判断这一题，显示下一题
			"""
			judge()

		self.f1_2 = Frame(self.root, height=380, width=600, bd=4, bg='PaleGreen')
		self.f1_2.place(x=0, y=0)
		ques()
		self.bt2 = Button(self.f1_2, text='确认', bd=2, width=8, command=judge)
		self.bt2.place(x=260, y=280)

	def en_to_ch(self):
		"""
		英--->汉
		"""
		self.model = 1
		self.wordChoice()

	def ch_to_en(self):
		"""
		汉--->英
		"""
		self.model = 0
		self.wordChoice()

	# 下面三个函数主要是查词、给个人词库中增词
	def haici(self, word):
		"""
		用"海词"网站查单词
		"""
		self.url = 'http://dict.cn/'
		self.url += word
		try:
			self.page = urllib.urlopen(self.url)  # 获取网页源代码
		except:
			return
		else:  # 正则匹配查找
			pattern1 = re.compile('<ul class="dict-basic-ul">([\s\S]*?)</ul>')
			pattern2 = re.compile('<span>(.*)</span>')
			pattern3 = re.compile('<strong>(.*)</strong>')
			self.data = self.page.read().decode('utf8')
			trans_content = re.findall(pattern1, self.data)
			trans1 = re.findall(pattern2, trans_content[0])
			trans2 = re.findall(pattern3, trans_content[0])
			trans_all = ''
			for i in range(min(len(trans1), len(trans2))):
				trans_all += trans1[i] + trans2[i] + '\n'
			if trans_content:
				return trans_all
			else:
				return None

	def addWords(self):
		def add_it():
			word = self.v4.get().lower()
			trans = self.haici(word)
			with open('Users/' + self.userName + '_addWords.txt', 'a+') as f:
				if trans != None:
					item = word + '   ' + trans + '\n'
					f.write(item)
					Label(self.top1, text='成功加入！').grid(row=2)
				else:
					Label(self.top1, text='查无此词！').grid(row=2)
			self.v4.set('')

		def ok(event):
			add_it()

		self.top1 = Toplevel()
		self.top1.wm_attributes('-topmost', 1)  # 使查词的子窗口始终置于最前面
		self.v4 = StringVar()
		self.e11 = Entry(self.top1, textvariable=self.v4, bd=2)
		self.e11.bind('<Return>', ok)
		self.e11.grid(padx=4, pady=4)
		self.bt3 = Button(self.top1, text='确认', command=add_it)
		self.bt3.grid()
		Label(self.top1, text='').grid(row=2)

	def searchWord(self):
		def search_it():
			word = self.v5.get().lower()
			trans = self.haici(word)
			if trans != None:
				tkMessageBox.showinfo(title='查询结果', message=trans)
			else:
				tkMessageBox.showinfo(title='查询结果', message='查无此词！')
			self.v5.set('')

		def ok(event):
			search_it()

		self.top2 = Toplevel()
		self.top2.wm_attributes('-topmost', 1)  # 子窗口置于最前面
		self.v5 = StringVar()
		self.e22 = Entry(self.top2, textvariable=self.v5, bd=2)
		self.e22.bind('<Return>', ok)
		self.e22.grid(padx=4, pady=4)
		self.bt4 = Button(self.top2, text='确认', command=search_it)
		self.bt4.grid()

	def analyseText(self, referenceText):
		"""
		从英文文章中分析出四六级单词
		"""
		self.filename = tkFileDialog.askopenfilename(
			filetypes=[("all files", "*")], initialdir='./Texts')
		try:
			self.f2 = open(self.filename, 'r')
			self.data = self.f2.read()
			self.data = self.data.lower()
			for ch in ",.;~!@#$%^&*()_+=-:":
				self.data = self.data.replace(ch, ' ')
			self.data = self.data.split()
			self.f2.close()
		except:
			tkMessageBox.showerror('Error', '无法打开文件\n%s'%str(sys.exc_info()[1]))
		if self.filename == ():
			tkMessageBox.showwarning('Warning', "请选择文件!")
			exit(0)
		else:
			tkMessageBox.showinfo('Info', '正在分析中，请稍等。。。')

		self.count_of_words = 0
		temp = self.filename.encode('utf8')
		self.word_of_text = open('Texts/word_in_%s.txt'%temp[temp.find('Texts')+6:temp.find('txt')-1], 'a+')  # 用来存放分析出的单词
		for line in open('Lexicon/' + referenceText):
			try:
				self.word = line.strip().split()[0]
				self.trans = line.strip().split()[1]
				if self.word in self.data:
					self.item = self.word + '   ' + self.trans + '\n'
					self.word_of_text.write(self.item)
					self.count_of_words += 1
			except:
				pass
		self.word_of_text.close()
		tkMessageBox.showinfo(message='析出单词共%s条\n请在 Texts文件夹中查看' % str(self.count_of_words))

	def analyseCET4(self):
		"""
		从文本中找四级单词
		"""
		self.analyseText('CET_4.txt')

	def analyseCET6(self):
		"""
		从文本中找六级单词
		"""
		self.analyseText('CET_6.txt')

	def about(self):
		"""
		软件信息
		"""

		def ok(event):
			self.top3.destroy()

		self.top3 = Toplevel()
		self.lb1 = Listbox(self.top3, fg='white', bg='black', height=4,width=30)
		self.lb1.insert(1, 'Author: Duan Yunzhi')
		self.lb1.insert(2, 'Made on: 2017/6/1')
		self.lb1.insert(3, 'Contact: d15821917291@gmail.com')
		self.lb1.insert(4, 'Personal Page: clouduan.github.io')
		self.lb1.bind('<Return>', ok)
		self.lb1.grid(padx=3, pady=4)
		self.top3.mainloop()

	def usersInfo(self):
		"""
		用户信息
		"""

		def ok(event):
			self.top4.destroy()

		self.top4 = Toplevel()
		self.lb2 = Listbox(self.top4, fg='white', bg='black', height=3)
		self.lb2.insert(1, 'Current User:')
		self.lb2.insert(1, self.userName)
		self.lb2.bind('<Return>', ok)
		self.lb2.grid(padx=3, pady=4)
		self.top4.mainloop()


wel_page = Log()
# 没有注册登录则避免显示软件主界面
try:
	if wel_page.state == True:
		main_page = MyApp()
except AttributeError:
	pass
