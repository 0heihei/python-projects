# -*- coding: utf-8 -*-
from Tkinter import *
import tkFont

root = Tk()
root.title('SJTU Temple')
c = Canvas(root, width=800, height=800, bg='white')

c.create_arc(200, 0, 400, 200, start=270, extent=90, style='arc', width=5)
c.create_arc(400, 0, 600, 200, start=180, extent=90, style='arc', width=5)
c.create_arc(150, 100, 350, 300, start=270, extent=90, style='arc', width=5)
c.create_arc(450, 100, 650, 300, start=180, extent=90, style='arc', width=5)
c.create_line(280, 295, 280, 400, width='5', fill='red')
c.create_line(510, 295, 510, 400, width='5', fill='red')
c.create_arc(360, 295, 430, 510, start=0, extent=180, style='arc', width=5)
ft = tkFont.Font(font=('黑体', 13, 'bold'))
c.create_text(400, 500, text='SJTU Temple', font=ft)
c.pack()

root.mainloop()
