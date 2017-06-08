# -*- coding: utf-8 -*-
from Tkinter import *

root = Tk()
root.title('凯旋门1')
c = Canvas(root, width=600, height=600, bg='skyblue')
c.pack()


def ground():
	r1 = c.create_polygon(110, 400, 400, 400, 520, 550, 0, 550, outline='', fill='gray')
	r2 = c.create_line(255, 400, 255, 550, fill='black')
	r3 = c.create_line(180, 400, 120, 550, fill='black')
	r4 = c.create_line(335, 400, 375, 550, fill='black')
	r5 = c.create_line(50, 500, 480, 500, fill='black')
	r5 = c.create_line(80, 450, 430, 450, fill='black')


def gate():
	r2 = c.create_rectangle(100, 100, 400, 180, outline='darkgray', fill='gainsboro')
	r3 = c.create_rectangle(100, 180, 200, 200, outline='darkgray', fill='gainsboro')
	r4 = c.create_rectangle(300, 180, 400, 200, outline='darkgray', fill='gainsboro')
	id1 = c.create_polygon(100, 200, 180, 200, 160, 220, 100, 220, outline='darkgray', fill='gainsboro')
	id2 = c.create_polygon(320, 200, 400, 200, 400, 220, 340, 220, outline='darkgray', fill='gainsboro')
	r5 = c.create_rectangle(100, 220, 160, 240, outline='darkgray', fill='gainsboro')
	r6 = c.create_rectangle(340, 220, 400, 240, outline='darkgray', fill='gainsboro')
	r7 = c.create_rectangle(100, 240, 140, 500, outline='darkgray', fill='gainsboro')
	r8 = c.create_rectangle(360, 240, 400, 500, outline='darkgray', fill='gainsboro')

	r11 = c.create_rectangle(150, 100, 350, 180, outline='darkgray', fill='lightgray')
	id3 = c.create_polygon(220, 110, 280, 110, 320, 140, 280, 170, 220, 170, 180, 140, fill='silver')
	r12 = c.create_rectangle(150, 100, 155, 180, outline='gainsboro', fill='silver')
	r13 = c.create_rectangle(345, 100, 350, 180, outline='gainsboro', fill='silver')

	l1 = c.create_line(100, 100, 400, 100, fill='darkgray')
	l2 = c.create_line(100, 180, 400, 180, fill='darkgray')

	l3 = c.create_line(100, 300, 140, 300, fill='darkgray')
	l4 = c.create_line(360, 300, 400, 300, fill='darkgray')
	l5 = c.create_line(100, 320, 140, 320, fill='darkgray')
	l6 = c.create_line(360, 320, 400, 320, fill='darkgray')


def sun():
	o1 = c.create_oval(500, 10, 580, 90, outline='red', fill='red')

	l7 = c.create_line(420, 80, 540, 40, fill='red')
	l8 = c.create_line(430, 60, 540, 30, fill='red')
	l9 = c.create_line(440, 40, 540, 20, fill='red')
	l11 = c.create_line(420, 100, 540, 50, fill='red')
	l12 = c.create_line(430, 120, 540, 60, fill='red')
	l13 = c.create_line(450, 140, 540, 70, fill='red')


def main():
	sun()
	ground()
	gate()
	root.mainloop()


main()
