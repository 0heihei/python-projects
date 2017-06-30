# -*- coding: utf-8 -*-
from Tkinter import *
import tkFont

root = Tk()
c = Canvas(root, width=1000, height=600, bg='skyblue')
c.pack()


def main():
	sun()  # 6
	roof()  # 1
	roofshadow()  # 2
	ground()  # 5
	gate()  # 3
	barrier()  # 4
	trees()
	root.mainloop()


def sun():  # 6
	for i in range(9):
		pie6_i = c.create_arc(800, 50, 920, 170, start=0 + i * 40, extent=20, fill='yellow', outline='')
	o6_2 = c.create_oval(815, 65, 905, 155, outline='', fill='skyblue')
	o6 = c.create_oval(820, 70, 900, 150, outline='', fill='red')


def roof():  # 1
	global p1_5, p1_6
	p1_1, p1_2, p1_3, p1_4, p1_5, p1_6 = (260, 210), (300, 150), (700, 150), (740, 210), (120, 280), (880, 280)
	poly1_1 = c.create_polygon(p1_5, p1_1, p1_2, p1_3, p1_4, p1_6, fill='dimgrey')
	roof_line = c.create_line(200, 250, 800, 250, fill='black')
	roof_line = c.create_line(270, 210, 730, 210, fill='black')
	roof_line = c.create_line(500, 150, 500, 300, fill='black')
	roof_line = c.create_line(400, 150, 380, 210, fill='black')
	roof_line = c.create_line(380, 210, 300, 300, fill='black')
	roof_line = c.create_line(600, 150, 620, 210, fill='black')
	roof_line = c.create_line(620, 210, 700, 300, fill='black')


def roofshadow():  # 2
	global p2_1, p2_2, p2_5, p2_7
	p2_1, p2_2, p2_3, p2_4, p2_5, p2_6, p2_7 = (240, 330), (760, 330), (120, 230), (880, 330), (360, 330), (640, 230), (
		640, 330)
	chord2_1 = c.create_arc(p2_3, p2_5, start=180, style='chord', fill='brown', outline='')
	chord2_2 = c.create_arc(p2_6, p2_4, start=270, style='chord', fill='brown', outline='')
	poly2_1 = c.create_polygon(p1_5, p2_1, p2_2, p1_6, fill='brown')
	for i in range(10):
		chord2_i = c.create_arc(240 + i * 50, 295, 275 + i * 50, 340, start=0, extent=180, style='chord',
								fill='darkred', outline='')


def ground():  # 5
	rec5_1 = c.create_rectangle(0, 450, 1000, 600, fill='gainsboro', outline='')


def gate():  # 3
	p3_1, p3_2, p3_3, p3_4, p3_5, p3_6 = (240, 470), (1000 - 240, 470), (360, 450), (1000 - 360, 450), (360, 470), (
		1000 - 360, 470)
	p3_7, p3_8, p3_9, p3_10 = (380, 450), (1000 - 380, 450), (380, 330), (1000 - 380, 330)
	p3_11, p3_12 = (360 + 90, 330), (1000 - 360 - 90, 450)
	line3_1 = c.create_line(0, 450, 1000, 450)
	rec3_1 = c.create_rectangle(p2_5, p3_4, fill='darkred', outline='')
	rec3_2 = c.create_rectangle(p2_1, p3_5, fill='lightsalmon', outline='')
	rec3_3 = c.create_rectangle(p2_7, p3_2, fill='lightsalmon', outline='')
	rec3_4 = c.create_rectangle(p3_11, p3_12, fill='white', outline='')
	poly3_1 = c.create_polygon(p2_5, p3_5, p3_7, p3_9, fill='sienna')
	poly3_2 = c.create_polygon(p3_10, p3_8, p3_6, p2_7, fill='sienna')
	ft = tkFont.Font(font=('黑体', 13, 'bold'))
	text3_1 = c.create_text(645, 340, text='交', anchor=NW, font=ft, )
	text3_2 = c.create_text(645, 370, text='通', anchor=NW, font=ft)
	text3_3 = c.create_text(645, 400, text='大', anchor=NW, font=ft)
	text3_4 = c.create_text(645, 430, text='学', anchor=NW, font=ft)


def barrier():  # 4
	p4_1, p4_2, p4_3, p4_4 = (120, 600), (1000 - 120, 600), (270, 500), (1000 - 270, 500)
	p4_5, p4_6, p4_7, p4_8, p4_9, p4_10 = (270, 420), (1000 - 270, 420), (0, 600), (1000, 600), (0, 520), (1000, 520)
	poly4_1 = c.create_polygon(p4_1, p4_3, p4_5, p4_9, p4_7, fill='white', outline='black')
	poly4_2 = c.create_polygon(p4_2, p4_4, p4_6, p4_10, p4_8, fill='white', outline='black')


def trees():
	t1 = c.create_oval(760, 380, 815, 490, fill="green")
	t2 = c.create_oval(190, 380, 250, 490, fill="green")
	p1 = c.create_polygon(786, 440, 796, 550, 776, 550)
	p2 = c.create_polygon(210, 550, 230, 550, 220, 440)


main()
