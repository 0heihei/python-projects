# encoding=utf8
#待修改，Linux版的为最优

from Tkinter import *
import tkMessageBox,tkFont
import time,random,re
import urllib2
import win32ui

#下面的类Log是为 登录界面 创建
class Log:
    def __init__(self):
        self.state =False            #初始状态为false，和最后几行切换出main_page有关
        self.r = Tk()
        self.r.title('非常背单词')
        self.r.geometry('300x125')
        self.name = StringVar()
        self.pswd = StringVar()  
        self.l1=Label(self.r, text='账号')
        self.l1.grid(row=3, column=1)
        self.l2=Label(self.r, text='密码')
        self.l2.grid(row=4, column=1)
        self.e1 = Entry(self.r, textvariable=self.name)
        self.e1.bind('<Return>', self.OK)      # 回车键确认
        self.e1.grid(row=3, column=2)
        self.e2 = Entry(self.r, textvariable=self.pswd,show='*')
        self.e2.bind('<Return>', self.OK)
        self.e2.grid(row=4, column=2)
        self.v1 = IntVar()  
        self.v1.set(1)
        self.rb1=Radiobutton(self.r, text='登录', variable=self.v1, value=1)
        self.rb1.grid(row=1, column=1, padx=30)
        self.rb2=Radiobutton(self.r, text='注册', variable=self.v1, value=0)
        self.rb2.grid(row=1, column=2, sticky=E)
        self.bt1=Button(self.r, text='确认', command=self.reg_or_log)
        self.bt1.grid(row=5, column=1)
        self.bt2=Button(self.r, text='重输', command=self.re_enter)
        self.bt2.grid(row=5, column=2, sticky=E)
        self.r.mainloop()

    def reg_or_log(self):
        self.getName = self.name.get().strip()
        self.getPswd = self.pswd.get().strip()
        if self.getName == '' or self.getPswd == '':            #用户未输入信息
            tkMessageBox.showwarning(self.r, message='请输入账号或密码！')
            self.re_enter()
            return
        elif not re.match('[a-zA-Z0-9]', self.getPswd):         #用正则判断格式
            tkMessageBox.showwarning(self.r, message='密码必须是字母和数字的组合！')
            self.re_enter()
            return
        else:               #得到合法输入，若是登录则判断，若是注册则保存用户信息
            self.userInfo = self.getName + '  ' + self.getPswd + '\n'
            with open('Users/usersInfo.dat', 'r') as self.f:
                self.userList = self.f.readlines()
                try:    # 下面操作字符串有时候会报错(转码错误)，故try
                    if self.v1.get() == 0:
                        if self.userInfo in self.userList:
                            tkMessageBox.showerror(message='用户名已存在!')
                            return  # 可以防止窗口关闭，使其停留在登录界面
                        else:
                            tkMessageBox.showinfo(self.r, message=' 成功注册！')
                            self.f.write(self.userInfo)
                            self.state= True
                    elif self.v1.get() == 1:
                        if self.userInfo in self.userList:
                            tkMessageBox.showinfo(self.r, message='成功登录！')
                            self.state = True
                        else:
                            tkMessageBox.showerror(self.r, message='用户名或密码错误！')
                            self.re_enter()
                            return
                finally:
                    self.f.close()
            self.r.destroy()

    def re_enter(self):           # 在输入错误的情况下把原先的内容清空以便重新输入
        self.pswd.set('')
        self.name.set('')

    def OK(self,event):
        self.reg_or_log()

class MyApp:
    def __init__(self):
        self.root = Tk()
        self.root.minsize(820,500)
        self.root.title('非常背单词')
        self.ft=tkFont.Font(font=('Microsoft YaHei',12,'normal'))      #字体默认微软雅黑
        self.userName=wel_page.getName      #后面要用到不同用户的用户名
        #以下菜单部分分为  出题的词库、出题的形式、本软件附加的功能、关于软件的其他信息
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
        #下面的frame是用来输出用户答题结果的部分
        self.f2_0 = Frame(self.root, height=125, width=600, bd=4, bg='DarkGray')
        self.f2_0.place(x=0, y=380)
        #下面的构件主要是 错词展示栏(misWords)和当前时间栏(l2)
        self.count_of_mis = 0        #做错的题目数量
        self.count_of_qs = 0         #做的总题目数量
        self.f3 = Frame(self.root, height=500, width=200, bd=4, bg='DimGray')
        self.f3.place(x=600, y=0)
        self.l1 = Label(self.f3, text='   <错词展示栏>    ' + '0/0', font=self.ft,fg='yellow', bg='DimGray')
        self.l1.place(x=0, y=0)
        self.misWords = Listbox(self.f3, height=480, width=300, fg='red', bg='SkyBlue')
        for i in range(700):
            self.misWords.insert(1, ' ')   # 必须首先填满Listbox，这样slide条才会出来
        self.sl = Scrollbar(self.root)
        self.sl.pack(side=RIGHT, fill=Y)
        self.misWords['yscrollcommand'] = self.sl.set
        self.sl['command'] = self.misWords.yview
        self.misWords.place(x=0, y=30)
        # 时间栏程序有参考别人的代码
        self.l2 = Label(self.f3,text="",height=2,width=28,bg='#383838',fg='white')
        self.l2.place(x=0, y=460)
        self.update_clock()

        self.root.mainloop()  # 按退格键出现乱码  则1系统自带输入法 2Ctrl+推个  3英文不会出现这样的问题

    def update_clock(self):
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.l2.configure(text=now)
        self.root.after(1000, self.update_clock)
        #下面4个函数总体来说就是获取词库单词
    def getFiles(self,name):   #打开相应词库文件，读取所有行(每行只有一个单词及其翻译)
        if name == '':     #不指定词库文件，给出文件对话框供用户选择
            self.fd = win32ui.CreateFileDialog(1)
            self.fd.SetOFNInitialDir('~/VocBank')
            self.fd.DoModal()
            self.filename = self.fd.GetPathName()
        else:
            self.filename = 'VocBank\\' + name

        try:         #用户打开文件对话框但是没有选择词库
            self.f1 = open(self.filename, 'r')
            self.lines = self.f1.readlines()
        finally:
            return
    def getWords(self):    #从之前的列表中选单词作为出题单词

        self.aLine, self.word, self.expre, self.word1, self.word2, self.word3, self.expre1, self.expre2, self.expre3 \
            = '', '', '', '', '', '', '', '', ''
        while '' in [self.aLine, self.word, self.expre, self.word1, self.word2,\
                     self.word3, self.expre1, self.expre2, self.expre3]:      # 词库文件有可能有空行会致错
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
                return None      #若返回 none 可表明用户没有选词库
        return True

    def getCET4(self):     #指定读取四级词汇
        self.getFiles('CET_4.txt')
    def getCET6(self):     #指定读取六级词汇
        self.getFiles('CET_6.txt')
    def getOthers(self):
        self.getFiles('')   # 此时就是 getFiles 中name 为空的情况
        # 填空题
    def wordCompletion(self):
        if self.getWords() == None:     # 防止用户未选词库就点击题型
            tkMessageBox.showerror(message='请先选择词库！')
            return
        tkMessageBox.showwarning(title='Tips', message='输完按 回车键 即可判断并切换')

        def ques():  #出题
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

        def judge(): #判断
            f2_1 = Frame(self.root, height=125, width=600, bd=4, bg='DarkGray')
            f2_1.place(x=0, y=380)

            f2 = Frame(f2_1, relief="groove", height=100, width=100)
            f2.place(x=180, y=0)
            if v2.get() == '' or v2.get().strip().lower() <> self.word:  ##答错则保存到错词本 "用户名+_misWords.txt"
                with open('Users/' + self.userName + '_misWords.txt', 'a+') as f:
                    item = self.word + '   ' + self.expre + '\n'
                    f.write(item)
                    f.close()
                wrong_ans = Label(f2, text='回答错误!\n' + '正确答案是  ' + self.word + '\n已为您添加至错词本！', width=25, font=self.ft)
                wrong_ans.grid()
                self.misWords.insert(0, item)   #答错的词上 错词展示榜
                self.count_of_mis +=1
            else:
                right_ans = Label(f2, text='回答正确！', width=25, font=1)
                right_ans.grid()
            self.count_of_qs +=1
            ques()
            self.l3 = Label(self.f3,text='   <错词展示栏>    ' + str(self.count_of_mis) + '/' + str(self.count_of_qs), font=self.ft,fg='yellow', bg='DimGray')   #更新  错误数/总题数
            self.l3.place(x=0, y=0)

        def next_one(event):
            judge()

        self.f1_1 = Frame(self.root, height=380, width=600, bd=4, bg='PaleGreen')
        self.f1_1.place(x=0, y=0)
        ques()
        self.bt1 = Button(self.f1_1, text='确认', bd=2, width=8, command=judge)
        self.bt1.place(x=265, y=240)
        #选择题
    def wordChoice(self):
        if self.getWords() == None:  # 防止用户未选词库就点击题型
            tkMessageBox.showerror(message='请先选择词库！')
            return
        tkMessageBox.showwarning(title='Tips', message='对着选项双击左键即可判断并切换')

        def ques():  #出题
            global v3,center,rightItem,rightAns
            self.getWords()
            if self.model == 1:   #英--->汉
                center, rightAns, ops2, ops3, ops4 = self.word, self.expre, self.expre1, self.expre2, self.expre3
            else:   #英--->汉
                center, rightAns, ops2, ops3, ops4 = self.expre, self.word, self.word1, self.word2, self.word3
            v3 = IntVar()
            ops = [rightAns, ops2, ops3, ops4]
            random.shuffle(ops)    #打乱顺序
            A, B, C, D = ops
            rightItem = ops.index(rightAns)    #提前找出正确选项

            f3 = Frame(self.f1_2, bd=4, relief="groove", height=100, width=100)
            f3.place(x=180, y=80)
            Label(f3, text=center, width=20, font=self.ft, bd=2).grid()
            rb1 = Radiobutton(f3, text=A, variable=v3, value=0, height=1,font=self.ft)
            rb2 = Radiobutton(f3, text=B, variable=v3, value=1, height=1,font=self.ft)
            rb3 = Radiobutton(f3, text=C, variable=v3, value=2, height=1,font=self.ft)
            rb4 = Radiobutton(f3, text=D, variable=v3, value=3, height=1,font=self.ft)
            rb1.bind('<Double-Button-1>', next_one)
            rb2.bind('<Double-Button-1>', next_one)
            rb3.bind('<Double-Button-1>', next_one)
            rb4.bind('<Double-Button-1>', next_one)
            rb1.grid(stick=W)
            rb2.grid(stick=W)
            rb3.grid(stick=W)
            rb4.grid(stick=W)

        def judge():  #判断
            f2_2 = Frame(self.root, height=125, width=600, bd=4, bg='DarkGray')
            f2_2.place(x=0, y=380)
            f4 = Frame(f2_2, relief="groove", height=100, width=100)
            f4.place(x=180, y=0)
            if v3.get() == rightItem:
                right_ans = Label(f4, text='回答正确！', width=25, font=self.ft)
                right_ans.grid()
            else:      #答错则保存到错词本 "用户名+_misWords.txt"
                with open('Users/' + self.userName + '_misWords.txt', 'a+') as f:
                    if self.model == 1:
                        item = center + '   ' + rightAns + '\n'
                    else:
                        item = rightAns + '   ' + center + '\n'
                    f.write(item)
                    f.close()
                wrong_ans = Label(f4, text='回答错误!\n' + '正确答案是  ' + rightAns + '\n已为您添加至错词本！', width=30,font=self.ft)
                wrong_ans.grid()
                self.misWords.insert(0, item)      #上榜
                self.count_of_mis += 1
            ques()
            self.count_of_qs += 1
            self.l4 = Label(self.f3, text='   <错词展示栏>    ' + str(self.count_of_mis) + '/' + str(self.count_of_qs), font=self.ft, fg='yellow', bg='DimGray')   #更新  错误数/总题数
            self.l4.place(x=0, y=0)

        def next_one(event):
            judge()

        self.f1_2 = Frame(self.root, height=380, width=600, bd=4, bg='PaleGreen')
        self.f1_2.place(x=0, y=0)
        ques()
        self.bt2 = Button(self.f1_2, text='确认', bd=2, width=8, command=judge)
        self.bt2.place(x=260, y=280)
    def en_to_ch(self):  #英--->汉
        self.model = 1
        self.wordChoice()
    def ch_to_en(self):  #汉--->英
        self.model = 0
        self.wordChoice()
    #下面三个函数主要是查词、给个人词库中增词
    def haici(self,word):  #用海词查单词
        self.url = 'http://dict.cn/'
        self.url += word
        try:
            self.page = urllib2.urlopen(self.url)    #获取网页源代码
        except:
            return   #没网不行
        else:    #网页保存为了字符串，查找标志词，确定单词翻译所在
            self.data = self.page.read()
            self.index_begin = self.data.find('class=\"dict-basic-ul\"')
            self.start = self.data.find('</span><strong>', self.index_begin)
            self.end = self.data.find('</strong></li>', self.index_begin)
            if self.start > 0:      # 当找不到标志性序列时就会返回 -1，大于0表示找到了
                return self.data[self.start + 15: self.end]
            else:
                return None
    def addWords(self):
        def add_it():
            word = self.v4.get().lower()
            trans = self.haici(word)
            with open('Users/' + self.userName + '_addWords.txt', 'a+') as f:  #个人词库为  "用户名+_addWords.txt"
                if trans <> None:
                    item = word + '   ' + trans + '\n'
                    f.write(item)
                    f.close()
                    Label(self.top1,text='成功加入！').grid(row=2)
                else:
                    Label(self.top1, text='查无此词！').grid(row=2)
            self.v4.set('')

        def OK(event):
            add_it()

        self.top1 = Toplevel()
        self.top1.wm_attributes('-topmost', 1)  # 子窗口置于最前面
        self.v4 = StringVar()
        self.e11 = Entry(self.top1, textvariable=self.v4,bd=2)
        self.e11.bind('<Return>', OK)
        self.e11.grid(padx=4,pady=4)
        self.bt3=Button(self.top1, text='确认', command=add_it)
        self.bt3.grid()
        Label(self.top1, text='').grid(row=2)
    def searchWord(self):
        def search_it():
            word = self.v5.get().lower()
            trans = self.haici(word)
            if trans <> None:
                tkMessageBox.showinfo(title='查询结果',message=trans)
            else:
                tkMessageBox.showinfo(title='查询结果',message='查无此词！')
            self.v5.set('')

        def OK(event):
            search_it()

        self.top2 = Toplevel()
        self.top2.wm_attributes('-topmost',1)            #子窗口置于最前面
        self.v5 = StringVar()
        self.e22 = Entry(self.top2, textvariable=self.v5,bd=2)
        self.e22.bind('<Return>', OK)
        self.e22.grid(padx=4,pady=4)
        self.bt4=Button(self.top2, text='确认', command=search_it)
        self.bt4.grid()

    def analyseText(self,referenceText):
        self.fd = win32ui.CreateFileDialog(1)
        self.fd.SetOFNInitialDir('~/Texts')
        self.fd.DoModal()
        try:         #用户打开了文件对话框但是没有选择要分析的文本
            self.filename = self.fd.GetPathName()   #文本文件一定要utf8编码，不然乱码(可用记事本 另存为 转化)
            self.f2 = open(self.filename, 'a+')
            self.data = self.f2.read()
            self.data = self.data.lower()
            for ch in ",.;~!@#$%^&*()_+=-:":   # 参考老师的课件，去除标点
                self.data = self.data.replace(ch, ' ')
            self.data = self.data.split()

            self.count_of_words = 0
            self.word_of_text = open('Texts/word_of_text.txt', 'a+')  #用来存放分析出的单词
            for line in open('VocBank/' + referenceText):
                try:        # 有时会发生 out of index（词库文件问题）
                    self.word = line.strip().split()[0]
                    self.trans = line.strip().split()[1]
                    if self.word in self.data:
                        self.item = self.word + '   ' + self.trans + '\n'
                        self.word_of_text.write(self.item)
                        self.count_of_words += 1
                except:
                    pass
            self.word_of_text.close()
            tkMessageBox.showinfo(message='析出单词共' + str(self.count_of_words) + '条\n请在 word_of_text.txt 中查看')
        finally:
            return
    def analyseCET4(self):   #从文本中找四级单词
        self.analyseText('CET_4.txt')
    def analyseCET6(self):   #从文本中找六级单词
        self.analyseText('CET_6.txt')

    def about(self):
        def OK(event):
            self.top3.destroy()

        self.top3 = Toplevel()
        self.lb1 = Listbox(self.top3, fg='white', bg='black', height=3)
        self.lb1.insert(1, 'Author: Duan Yunzhi')
        self.lb1.insert(2, 'Made on: 2016/12/30')
        self.lb1.bind('<Return>', OK)
        self.lb1.grid(padx=3,pady=4)
        self.top3.mainloop()
    def usersInfo(self):
        def OK(event):
            self.top4.destroy()

        self.top4 = Toplevel()
        self.lb2 = Listbox(self.top4, fg='white', bg='black', height=3)
        self.lb2.insert(1, 'Current User:')
        self.lb2.insert(1,self.userName)
        self.lb2.bind('<Return>', OK)
        self.lb2.grid(padx=3,pady=4)
        self.top4.mainloop()

wel_page=Log()
try:          #没有注册登录则避免显示软件主界面
    if wel_page.state == True:
        main_page = MyApp()
except AttributeError:
    pass
