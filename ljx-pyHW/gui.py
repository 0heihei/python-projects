from Tkinter import *

class GUInterface:
    def __init__(self):
        self.root = Tk()
        self.root.title("Identity Check")
        self.id = StringVar()
        self.id.set('')
        self.ready=''
        self.flag=False
        self.where = StringVar()
        self.gender = StringVar()
        self.check = StringVar()
        self.a = Entry(self.root, textvariable=self.id)
        self.a.pack()
        self.b = Entry(self.root, textvariable=self.where)
        self.b.pack()
        self.c = Entry(self.root, textvariable=self.gender)
        self.c.pack()
        self.d = Entry(self.root, textvariable=self.check)
        self.d.pack()
        self.e=Button(self.root,text='ok',command=self.ok)
        self.e.pack()
        self.f=Button(self.root,text='quit',command=self.close)
        self.f.pack()


    def getInfo(self):
        self.root.mainloop()
        return self.id.get(),self.flag

    def showInfo(self, a, b, c):
        self.check.set(a)
        self.where.set(b)
        self.gender.set(c)
    def ok(self):
        self.ready='ok'
        self.ID=self.id.get()
        self.root.quit()
    def close(self):
        self.flag = True
        self.root.quit()
        self.root.destroy()