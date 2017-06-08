# -*- coding:utf-8 -*-

from Tkinter import *

root = Tk()
root.title('南区体育馆')
c = Canvas(root, height=600, width=1000, bg='white')
c.pack()

c.create_rectangle(0, 0, 1000, 250, fill='skyblue', outline='')
c.create_rectangle(0, 250, 1000, 600, fill='lightgreen', outline='')

c.create_oval(100, 70, 300, 150, fill='white', outline='')
c.create_oval(400, 200, 500, 225, fill='white', outline='')
c.create_oval(650, 30, 900, 110, fill='white', outline='')

c.create_polygon(100, 300, 150, 230, 350, 230, 300, 300, fill='grey', outline='black')
c.create_rectangle(100, 300, 300, 590, fill='grey')
c.create_polygon(300, 300, 350, 230, 350, 520, 300, 590, fill='grey', outline='black')

c.create_rectangle(180, 330, 230, 380, fill='darkgrey')
c.create_rectangle(180, 400, 230, 450, fill='darkgrey')
c.create_rectangle(180, 470, 230, 520, fill='darkgrey')
c.create_rectangle(250, 550, 270, 590, fill='darkgrey')

c.create_oval(400, 300, 950, 500, fill='darkred', outline='')
c.create_oval(440, 340, 910, 460, fill='darkgreen', outline='')
c.create_oval(410, 310, 940, 490, fill='', outline='white')
c.create_oval(420, 320, 930, 480, fill='', outline='white')
c.create_oval(430, 330, 920, 470, fill='', outline='white')

root.mainloop()
