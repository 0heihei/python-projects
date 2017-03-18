# encoding=utf8
import random
import time
from Tkinter import *
from tkMessageBox import *
import re

def wel_page():
    def reg_or_log():
        global userName
        userName = name.get().strip()
        userPswd = pswd.get().strip()
        if userName == '' or userPswd == '':
            showwarning(r,message='请输入账号或密码！')
            re_enter()
            return
        elif not re.match('[a-zA-Z0-9]',userPswd):
            showwarning(r,message='密码必须是字母和数字的组合！')
            re_enter()
            return
        else:
            n_and_p=userName+'  '+userPswd+'\n'     #必须加'\n'
            with open('usersInfo.dat', 'a+') as f:
                userList = f.readlines()
                try:      #下面操作字符串有时候会报错(转码错误)，故try
                    if v.get() == 0:
                        if n_and_p in userList:
                            showerror(message='您已注册，不能重新注册!')
                            v.set(1)  #自动调成登录按钮
                            return  # 可以防止窗口关闭，使其停留在登录界面，记忆价值的tips
                        else:
                            showinfo(r, message=' 成功注册！')
                            f.write(n_and_p)
                    elif v.get() == 1:
                        if n_and_p in userList:
                            showinfo(r, message='成功登录！')
                        else:
                            showerror(r, message='用户名或密码错误！')
                            re_enter()
                            return
                except:
                    pass

                f.close()
            r.destroy()

    def re_enter():     #在输入错误的情况下把原先的内容清空以便重新输入
        pswd.set('')
        name.set('')

    def OK(event):
        reg_or_log()

    r=Tk()
    r.title('玩转英语单词')
    r.geometry('300x125')
    name = StringVar()
    pswd = StringVar()  # 此处变量名不好
    Label(r, text='账号').grid(row=3, column=1)
    Label(r, text='密码').grid(row=4, column=1)
    entryName = Entry(r, textvariable=name)
    entryName.bind('<Return>',OK)     #回车键确认
    entryName.grid(row=3, column=2)
    entryPswd = Entry(r, textvariable=pswd)
    entryPswd.bind('<Return>',OK)
    entryPswd.grid(row=4, column=2)
    v=IntVar()                                #这个括号一定不能忘
    v.set(1)
    Radiobutton(r, text='登录', variable=v,value=1).grid(row=1,column=1,padx=30)
    Radiobutton(r, text='注册', variable=v,value=0).grid(row=1,column=2,sticky=E)
    Button(r,text='确认',command=reg_or_log).grid(row=5,column=1)
    Button(r,text='重输',command=re_enter).grid(row=5,column=2,sticky=E)
    r.mainloop()

userName='admin'
############################################################################
#from ttk import *
from tkMessageBox import *
import random
import urllib,urllib2
import win32ui


def getFiles(name):
    global lines
    if name == '':
        flist = win32ui.CreateFileDialog(1)
        flist.SetOFNInitialDir('E:\Python35Project\CT_exs\BigProject\VocabularyBank')
        flist.DoModal()
        filename = flist.GetPathName()
    else:
        filename='E:\Python35Project\CT_exs\BigProject\VocabularyBank\\'+name    #unicode('E:\Python35Project\程设作业\大作业\单词库\\'+name,'utf8') #重点:此处可用//，也可用/代替

    f = open(filename, 'r')
    lines = f.readlines()
def getWords():
    global aWord,oWord1,oWord2,oWord3,aExpre,oExpre1,oExpre2,oExpre3

    aLine, aWord, aExpre, oWord1, oWord2, oWord3, oExpre1, oExpre2, oExpre3='','','','','','','','',''
    while '' in [aLine,aWord,aExpre,oWord1,oWord2,oWord3,oExpre1,oExpre2,oExpre3]:   #防止读到空行
        aLine = lines[random.randint(1, len(lines))]
        aWord = aLine.split()[0].strip()
        aExpre = aLine.split()[1].strip()
        oWord1 = lines[random.randint(1, len(lines))].split()[0].strip()
        oWord2 = lines[random.randint(1, len(lines))].split()[0].strip()
        oWord3 = lines[random.randint(1, len(lines))].split()[0].strip()
        oExpre1 = lines[random.randint(1, len(lines))].split()[1].strip()
        oExpre2 = lines[random.randint(1, len(lines))].split()[1].strip()
        oExpre3 = lines[random.randint(1, len(lines))].split()[1].strip()

def getCET4():
    getFiles('CET_4.txt')
def getCET6():
    getFiles('CET_6.txt')
def getOthers():
    getFiles('')

def wordCompletion():         #给出首字母补全单词
    global mark
    mark=1

    try:                    #防止用户未选词库就点击题型
        getWords()
    except NameError:
        showerror(message='请先选择词库！')
        return
    showwarning(title='Tips', message='输完按 回车键 即可判断并切换')
    def ques():
        global v
        getWords()
        f1 = Frame(framework1_1, bd=4, relief="groove", height=100, width=100)
        f1.place(x=165, y=100)
        Label(f1, text=aExpre, height=3, width=30, font=0).grid()
        v = StringVar()
        entryWord = Entry(f1, width=20, bd=2, textvariable=v)
        entryWord.bind('<Return>', next_one)
        entryWord.grid()
        Label(f1,text=' ').grid()    #为界面美观而加入无其他作用

    def judge():
        framework2_1 = Frame(root, height=200, width=600, bd=4, bg='DimGray')
        framework2_1.place(x=0, y=400)

        f2=Frame(framework2_1,relief="groove", height=100, width=100)
        f2.place(x=180,y=0)
        if v.get() == '' or v.get().strip().lower() <> aWord:
            with open('E:\Python35Project\CT_exs\BigProject\users/'+userName+'_misWords.txt','a+') as f:
                item = aWord + ' ' + aExpre + '\n'
                f.write(item)
                f.close()
            wrong_ans=Label(f2,text='回答错误!\n' + '正确答案是  ' + aWord + '\n已为您添加至错词本！',width=25,font=1)
            wrong_ans.grid()
            misWords.insert(0,item)
        else:
            right_ans=Label(f2,text='回答正确！',width=25,font=1)
            right_ans.grid()
        ques()

    def next_one(event):
        judge()

    framework1_1 = Frame(root, height=400, width=600, bd=4, bg='green')
    framework1_1.place(x=0, y=0)
    ques()
    b2 = Button(framework1_1, text='确认', bd=2, width=8, command=judge)
    b2.place(x=265, y=240)

def wordChoice():
    global mark
    mark=0
    try:                    #防止用户未选词库就点击题型
        getWords()
    except NameError:
        showerror(message='请先选择词库！')
        return
    showwarning(title='快捷键',message='对着选项双击左键即可判断并切换')

    def ques():
        global v,rightAns,rightItem,center
        getWords()
        if model == 1:
            center, rightAns, option2, option3, option4 = aWord, aExpre, oExpre1, oExpre2, oExpre3
        else:
            center, rightAns, option2, option3, option4 = aExpre, aWord, oWord1, oWord2, oWord3
        v = IntVar()
        option = [rightAns, option2, option3, option4]
        random.shuffle(option)
        A, B, C, D = option
        rightItem = option.index(rightAns)

        f3 = Frame(framework1_2, bd=4, relief="groove", height=100, width=100)
        f3.place(x=180, y=100)
        Label(f3, text=center, height=2, width=25, font=0, bd=2).grid()
        rb1=Radiobutton(f3, text=A, variable=v, value=0,height=1)
        rb2=Radiobutton(f3, text=B, variable=v, value=1,height=1)
        rb3=Radiobutton(f3, text=C, variable=v, value=2,height=1)
        rb4=Radiobutton(f3, text=D, variable=v, value=3,height=1)
        rb1.bind('<Double-Button-1>',next_one)
        rb2.bind('<Double-Button-1>',next_one)
        rb3.bind('<Double-Button-1>',next_one)
        rb4.bind('<Double-Button-1>',next_one)
        rb1.grid(stick=W)
        rb2.grid(stick=W)
        rb3.grid(stick=W)
        rb4.grid(stick=W)

    def judge():
        framework2_2 = Frame(root, height=200, width=600, bd=4, bg='DimGray')
        framework2_2.place(x=0, y=400)
        f4 = Frame(framework2_2, relief="groove", height=100, width=100)
        f4.place(x=180, y=0)
        if v.get() == rightItem:
            right_ans = Label(f4, text='回答正确！', width=25, font=1)
            right_ans.grid()
        else:
            with open('E:\Python35Project\CT_exs\BigProject\users/' + userName + '_misWords.txt', 'a+') as f:
                if model == 1:
                    item = center + ' ' + rightAns + '\n'
                else:
                    item = rightAns + ' ' + center + '\n'
                f.write(item)
                f.close()
            wrong_ans = Label(f4, text='回答错误!\n' + '正确答案是  ' + rightAns + '\n已为您添加至错词本！', width=30)
            wrong_ans.grid()
            misWords.insert(0, item)
        ques()

    def next_one(event):
        judge()

    framework1_2 = Frame(root, height=400, width=600, bd=4, bg='green')
    framework1_2.place(x=0, y=0)
    ques()
    b2=Button(framework1_2, text='确认', bd=2,width=8,command=judge)
    b2.place(x=260,y=280)
def en_to_ch():
    global model
    model=1
    wordChoice()
def ch_to_en():
    global model
    model=0
    wordChoice()

def haici(word):
    url = 'http://dict.cn/'
    url += word
    try:
        page = urllib2.urlopen(url)
    except:
        return
    else:
        data = page.read()
        index_begin = data.find('class=\"dict-basic-ul\"')
        start = data.find('</span><strong>', index_begin)
        end = data.find('</strong></li>', index_begin)
        if start > 0:  # 当找不到那些序列时就会返回 -1，因此可以用大于0筛选
            return data[start + 15: end]
        else:
            showerror(message='单词不存在')
def addWords():
    def add_it():
        word=v.get().lower()
        trans = haici(word)
        with open('E:\Python35Project\CT_exs\BigProject\users/'+userName+'_addWords.txt','a+') as f:
            if trans <> None:
                item = word + ' ' + trans + '\n'
                f.write(item)
                f.close()
                showinfo(message='成功加入！')
            else:
                showerror(message='查无此词！')
        v.set('')
    def OK(event):
        add_it()

    top = Toplevel()
    v = StringVar()
    entryWord = Entry(top, textvariable=v)
    entryWord.bind('<Return>', OK)
    entryWord.grid()
    Button(top, text='确认', command=add_it).grid()
def searchWord():
    def search_it():
        word = v.get().lower()
        trans=haici(word)
        if trans <> None:
            showinfo(message=trans)
        v.set('')
    def OK(event):
        search_it()
    top=Toplevel()
    v = StringVar()
    entryWord=Entry(top, textvariable=v)
    entryWord.bind('<Return>',OK)
    entryWord.grid()
    Button(top, text='确认', command=search_it).grid()
def analyseText(referenceText):
    flist = win32ui.CreateFileDialog(1)
    flist.SetOFNInitialDir('E:\Python35Project\CT_exs\BigProject\VocabularyBank')
    flist.DoModal()
    filename = flist.GetPathName()
    f = open(filename, 'r')
    data = f.read()
    data = data.lower()
    for ch in ",.;~!@#$%^&*()_+=-:":
        data = data.replace(ch, ' ')
    data = data.split()

    count = 0
    word_of_text=open('E:\Python35Project\CT_exs\BigProject\VocabularyBank/word_of_text.txt','a+')
    for line in open('E:\Python35Project\CT_exs\BigProject\VocabularyBank/'+referenceText):
        try:               #有时会发生 out of index（文件问题）
            word = line.split()[0]
            trans = line.split()[1]
        except:
            pass
        if word in data:
            item=word +'  ' + trans+ '\n'
            word_of_text.write(item)
            count += 1
    word_of_text.close()
    showinfo(message='析出单词共计'+str(count)+'条\n请在 word_of_text 文本文件中查看')
def analyseCET4():
    analyseText('CET_4.txt')
def analyseCET6():
    analyseText('CET_6.txt')

def about():
    def OK(event):
        top.destroy()
    top=Toplevel()
    lb=Listbox(top,fg='white',bg='black',height=3)
    lb.insert(1,'Author: Duan Yunzhi')
    lb.insert(2,'Made on: 2016/12/20')
    lb.bind('<Return>',OK)
    lb.grid()
    top.mainloop()
def usersInfo():
    def OK(event):
        top.destroy()
    top=Toplevel()
    lb=Listbox(top,fg='white',bg='black',height=3)
    lb.insert(1,'Current User:'+userName)
    lb.bind('<Return>',OK)
    lb.grid()
    top.mainloop()


root = Tk()
root.geometry('800x500')
root.title('非常玩单词')

framework3 = Frame(root,height = 500,width = 200,bd=4,bg='DimGray')
framework3.place(x=600,y=0)
Label(framework3, text='@错词展示栏@',font=1,fg='yellow',bg='DimGray').place(x=640,y=0)
misWords=Listbox(framework3,height = 500,width = 300,fg='red',bg='SkyBlue')
for i in range(700):
    misWords.insert(1,' ')        #必须首先填满Listbox，这样slide条才会出来
scrollbar = Scrollbar(framework3)
scrollbar.pack(side=RIGHT, fill=Y)
misWords['yscrollcommand'] = scrollbar.set
scrollbar['command'] = misWords.yview
misWords.place(x=600,y=30)

Frame(root,height=200,width=600,bd=4,bg='DimGray').place(x=0,y=400)

m = Menu(root)
root.config(menu = m)
menu1 = Menu(m)                                            #####
m.add_cascade(label="词库", menu=menu1)
menu1.add_command(label="四级", command=getCET4)
menu1.add_command(label="六级", command=getCET6)
menu1.add_command(label="其它", command=getOthers)

menu2 = Menu(m)                                            #####
m.add_cascade(label="样式", menu=menu2)
menu2.add_command(label="填空题", command=wordCompletion)
menu21=Menu(menu2)
menu2.add_cascade(label='选择题',menu=menu21)
menu21.add_command(label='英-->汉',command=en_to_ch)
menu21.add_command(label='汉-->英',command=ch_to_en)

menu3=Menu(m)
m.add_cascade(label='功能',menu=menu3)
menu3.add_command(label='增词',command=addWords)
menu3.add_command(label='查词',command=searchWord)
menu31=Menu(menu3)
menu3.add_cascade(label='分析',menu=menu31)
menu31.add_command(label='四级词汇',command=analyseCET4)
menu31.add_command(label='六级词汇',command=analyseCET6)

menu4=Menu(m)                                              #####
m.add_cascade(label="关于", menu=menu4)
menu4.add_command(label='信息',command=about)
menu4.add_command(label='用户',command=usersInfo)


root.mainloop()    #按退格键出现乱码  则1系统自带输入法 2Ctrl+推个  3英文不会出现这样的问题

