#-*- coding:utf-8 -*-

from Tkinter import *

root = Tk()
root.title('思源湖畔-教学楼')
c = Canvas(root, width=600, height=400, bg="skyblue")
c.pack()


def main():
	drawGrass()
	drawLake()
	drawTrees()
	drawSun()
	drawBuildings()
	root.mainloop()


def drawGrass():
	for j in range(15):
		k = 140 + j * 20
		l = 120 + j * 20
		u = 160 + j * 20
		g = c.create_line(1, k, 100, l, 200, k, 300, u, 400, k, 500, l, 599, u, smooth=1, fill="green", width=3)


def drawLake():
	a = c.create_oval(200, 150, 580, 300)
	c.itemconfig(a, fill="blue")


def drawTrees():
	drawOval()
	drawPolygons()


def drawOval():
	t1 = c.create_oval(520, 180, 575, 290, fill="green")
	t2 = c.create_oval(460, 210, 520, 320, fill="green")


def drawPolygons():
	p1 = c.create_polygon(546, 240, 556, 350, 536, 350)
	p2 = c.create_polygon(480, 380, 500, 380, 490, 270)


def drawSun():
	for i in range(9):
		pie6_i = c.create_arc(520, 20, 570, 70, start=0 + i * 40, extent=20, fill='yellow', outline='')
	s1 = c.create_oval(525, 25, 565, 65, fill="skyblue", outline='')
	s2 = c.create_oval(530, 30, 560, 60, fill="red", outline='')


def drawBuildings():
	drawMain()
	drawWindows()
	drawDoors()


def drawMain():
	b1 = c.create_rectangle(55, 90, 195, 345, fill="brown")
	x1 = c.create_polygon(55, 90, 85, 60, 225, 60, 195, 90, fill="grey", outline="black")
	x2 = c.create_polygon(195, 90, 225, 60, 225, 315, 195, 345, fill="grey", outline="black")
	b2 = c.create_rectangle(195, 160, 325, 335, fill="brown")
	x3 = c.create_polygon(195, 160, 325, 160, 355, 130, 225, 130, fill="grey", outline="black")
	x4 = c.create_polygon(325, 160, 355, 130, 355, 300, 325, 335, fill="grey", outline="black")


def drawWindows():
	for i in range(4):
		a = 100 + i * 50
		b = 130 + i * 50
		w1 = c.create_rectangle(75, a, 105, b, fill="white")
		w2 = c.create_rectangle(145, a, 175, b, fill="white")
	for m in range(2):
		q = 180 + m * 50
		p = 210 + m * 50
		w3 = c.create_rectangle(215, q, 245, p, fill="white")
		w4 = c.create_rectangle(275, q, 305, p, fill="white")


def drawDoors():
	d1 = c.create_rectangle(95, 300, 120, 345)
	d2 = c.create_rectangle(120, 300, 145, 345)
	o1 = c.create_oval(115, 320, 120, 325)
	o2 = c.create_oval(120, 320, 125, 325)
	d3 = c.create_rectangle(235, 290, 260, 335)
	d4 = c.create_rectangle(260, 290, 285, 335)
	o3 = c.create_oval(255, 310, 260, 315)
	o4 = c.create_oval(260, 310, 265, 315)


main()
