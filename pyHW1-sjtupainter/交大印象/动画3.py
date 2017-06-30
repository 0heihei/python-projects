# -*- coding: utf-8 -*-
from Tkinter import *
from time import sleep
from math import pi, cos, sin

root = Tk()
root.title('新图A200')
c = Canvas(root, width=480, height=640, bg='white')
c.pack()


def backwall():
	b1()
	b2()
	b3()


def b1():
	s1 = (152, 0)
	s2 = (176, 167.2)
	s3 = (304, 108)
	s4 = (320, 0)
	s5 = (308, 0)
	s6 = (300, 58.4)
	s7 = (175.2, 132)
	s8 = (160, 0)
	b1 = c.create_polygon(s1, s2, s3, s4, s5, s6, s7, s8, outline='brown', fill='LemonChiffon')


def b2():
	s1 = (92.8, 0)
	s2 = (179.2, 284.8)
	s3 = (310.4, 235.2)
	s4 = (401.6, 0)
	s5 = (356.8, 0)
	s6 = (307.2, 187.2)
	s7 = (177.6, 240.8)
	s8 = (114.4, 0)
	b2 = c.create_polygon(s1, s2, s3, s4, s5, s6, s7, s8, outline='brown', fill='LemonChiffon')


def b3():
	s1 = (0, 206.4)
	s2 = (180.8, 428)
	s3 = (320, 408)
	s4 = (480, 251.2)
	s5 = (480, 48.8)
	s6 = (317.6, 329.6)
	s7 = (180.8, 368)
	s8 = (0, 29.6)
	b3 = c.create_polygon(s1, s2, s3, s4, s5, s6, s7, s8, outline='brown', fill='LemonChiffon')


def windows():
	for i in range(3):
		s1 = (190 + i * 32, 103.8 - i * 20)
		s2 = (190 + i * 32, 117.4 - i * 20)
		s3 = (216.4 + i * 32, 103 - i * 20)
		s4 = (216.4 + i * 32, 88.6 - i * 20)
		wi = c.create_polygon(s1, s2, s3, s4, outline='PaleTurquoise1', fill='AntiqueWhite1')


def stairs():
	st1()
	st2()
	st3()
	st4()


def st1():
	s11 = (185.6, 142.4, 352.8, 260.8)
	o11 = c.create_arc(s11, start=58, extent=122, outline='LightPink', fill='LightPink')
	s12 = (186.4, 152.8, 362.4, 260.8)
	o12 = c.create_arc(s12, start=67, extent=207, outline='LightPink2', fill='LightPink2')
	s13 = (235.2, 174.4, 330.4, 238.4)
	o13 = c.create_oval(s13, outline='white', fill='white')
	o131 = c.create_arc(s13, start=199, extent=207, style='chord', outline='brown', fill='LemonChiffon')
	o132 = c.create_arc(s13, start=199, extent=207, style='arc', outline='LemonChiffon')
	o133 = c.create_arc(s13, start=283, extent=135, style='chord', outline='white', fill='white')
	s1 = (309.4, 177.6)
	s2 = (290.2, 238.4)
	s3 = (311.2, 235.2)
	s4 = (328, 188.8)
	s5 = (305.6, 190.4)
	m1 = c.create_polygon(s1, s2, s3, s4, outline='LemonChiffon', fill='LemonChiffon')
	c.create_line(s3, s4, fill='brown')
	c.create_line(s1, s5, fill='brown')


def st2():
	s21 = (180.8, 231.2, 372, 349.6)
	o21 = c.create_arc(s21, start=60, extent=120, outline='PaleVioletRed1', fill='PaleVioletRed1')
	s22 = (181.6, 240.8, 368.8, 359.2)
	o22 = c.create_arc(s22, start=64, extent=207, outline='PaleVioletRed3', fill='PaleVioletRed3')
	s23 = (235.2, 260.8, 367.2, 339.2)
	o23 = c.create_oval(s23, outline='white', fill='white')
	o231 = c.create_arc(s23, start=276, extent=126, style='chord', outline='brown', fill='LemonChiffon')
	o232 = c.create_arc(s23, start=276, extent=126, style='arc', outline='LemonChiffon')


def st3():
	s31 = (178.4, 322.4, 436, 438.4)
	o31 = c.create_arc(s31, start=80, extent=110, outline='VioletRed1', fill='VioletRed1')
	s32 = (179.2, 337.6, 457.6, 438.4)
	o32 = c.create_arc(s32, start=88, extent=175, outline='VioletRed3', fill='VioletRed3')
	s33 = (235.2, 344.8, 392, 423.2)
	o33 = c.create_oval(s33, outline="LemonChiffon", fill='LemonChiffon')
	o331 = c.create_arc(s33, start=230, extent=115, style='chord', outline='brown', fill='white')
	o332 = c.create_arc(s33, start=230, extent=115, style='arc', outline='white')
	o333 = c.create_arc(s33, start=262, extent=140, style='chord', outline='brown', fill='white')
	o334 = c.create_arc(s33, start=262, extent=140, style='arc', outline='white')
	s1 = (320.5, 406.4)
	s2 = (304, 422.4)
	c.create_line(s1, s2, fill='white')


def st4():
	s41 = (180.8, 420, 480, 568)
	o41 = c.create_arc(s41, start=85, extent=120, outline='DeepPink2', fill='DeepPink2')
	s42 = (181.6, 435.2, 480, 568)
	o42 = c.create_arc(s42, start=87, extent=185, outline='DeepPink4', fill='DeepPink4')
	s43 = (225.6, 449.6, 468, 536)
	o43 = c.create_oval(s43, outline="white", fill='white')
	s1 = (397, 334)
	s2 = (414, 572)
	s3 = (446, 584)
	s4 = (414, 316)
	p32 = c.create_polygon(s1, s2, s3, s4, outline='Coral2', fill='Coral2')


def floor():
	s1 = (0, 660)
	s2 = (0, 610)
	s3 = (160, 540)
	s4 = (340, 540)
	s5 = (480, 600)
	s6 = (480, 660)
	f = c.create_polygon(s1, s2, s3, s4, s5, s6, outline='Coral4', fill='Coral4')


def pillars():
	p1()
	p2()
	p3()


def p1():
	s1 = (145, 0)
	s2 = (74, 727)
	s3 = (115, 727)
	s4 = (157, 0)
	p1 = c.create_polygon(s1, s2, s3, s4, outline='white', fill='Coral1')


def p2():
	s1 = (171, 108)
	s2 = (155, 727)
	s3 = (188, 727)
	s4 = (176, 148)
	p2 = c.create_polygon(s1, s2, s3, s4, outline='white', fill='Coral3')


def p3():
	s1 = (372, 0)
	s2 = (426, 770)
	s3 = (466, 770)
	s4 = (382, 0)
	p3 = c.create_polygon(s1, s2, s3, s4, outline='white', fill='Coral2')


def somebody():
	eX = [269, 282, 276, 301, 307, 313, 330, 347, 0]
	eY = [142, 174, 231, 260, 322, 344, 420, 450, 0]
	X = [269, 280, 276, 299, 307, 311, 330, 343]
	Y = [142, 174, 231, 260, 322, 344, 420, 450]
	mY = [210, 216, 300, 310, 390, 394, 504, 503]
	start = [0.3, 1, 0.35, 1, 0.45, 1, 0.45, 1]
	stop = [0.9, 1.3, 0.9, 1.2, 0.9, 1.45, 0.9, 1.45]
	a = [84, 48, 96, 66, 129, 78, 150, 121]
	b = [59, 32, 59, 39, 58, 39, 74, 43]

	person = c.create_oval(262, 116, 277, 131, fill='LawnGreen', outline='LawnGreen')
	for i in range(8):
		t = pi * start[i]
		while t < pi * stop[i]:
			t = t + 0.01 * pi
			new_eX = eX[i] + a[i] * cos(t)
			new_eY = mY[i] - b[i] * sin(t)

			edx = new_eX - X[i]
			edy = new_eY - Y[i]

			c.move(person, edx, edy)
			c.update()

			X[i] = new_eX
			Y[i] = new_eY

			sleep(0.05)

		c.delete(person)
		d = i + 1
		person = c.create_oval(eX[d] - 7, eY[d] - 26, eX[d] + 8, eY[d] - 11, fill='LawnGreen', outline='LawnGreen')


def main():
	pillars()
	backwall()
	windows()
	floor()
	stairs()
	somebody()
	root.mainloop()


main()
