# -*- coding:utf-8 -*-
from graphics import *


def main():
	w = GraphWin('人字拖', 600, 400)
	w.setBackground('deepskyblue')
	di(w)
	baiyun(w)
	lou(w)
	shu(w)
	qi(w)
	ren(w)
	men(w)
	logo(w)
	w.mainloop()


def di(win):
	r = Rectangle(Point(0, 320), Point(600, 400))
	r.setOutline('grey')
	r.setFill('grey')
	r.draw(win)


def baiyun(win):
	DrawYun(30, 100, win, 5)
	DrawYun(150, 30, win, 3)
	DrawYun(400, 50, win, 4)
	DrawYun(500, 70, win, 4)


def DrawYun(x, y, win, size):
	S = [[3, 3, 4], [4, -3, 3], [7, 2, 3], [0, -3, 4], [-3, 5, 3], [-5, -3, 3], [-7, 2, 3], [-3, 0, 3]]
	for i in S:
		c = Circle(Point(x + size * i[0], y + size * i[1]), size * i[2])
		c.setOutline('white')
		c.setFill('white')
		c.draw(win)


def ren(win):
	DrawRen(400, 320, win, 1)
	DrawRen(390, 315, win, 1)
	DrawRen(160, 320, win, 1)
	DrawRen(200, 340, win, 1)
	DrawRen(180, 375, win, 2)
	DrawRen(400, 380, win, 2)
	DrawRen(320, 350, win, 1)


def DrawRen(x, y, win, k):
	c = Circle(Point(x, y), 5 * k)
	c.setFill('black')
	c.draw(win)
	p0 = Point(x - 2 * k, y + 2 * k)
	p1 = Point(x + 2 * k, y + 2 * k)
	p2 = Point(x + 2 * k, y + 6 * k)
	p3 = Point(x + 5 * k, y + 4 * k)
	p4 = Point(x + 6 * k, y + 6 * k)
	p5 = Point(x + 2 * k, y + 8 * k)
	p6 = Point(x + 2 * k, y + 10 * k)
	p7 = Point(x + 4 * k, y + 13 * k)
	p8 = Point(x + 3 * k, y + 14 * k)
	p9 = Point(x, y + 10 * k)
	p16 = Point(x - 2 * k, y + 6 * k)
	p15 = Point(x - 5 * k, y + 4 * k)
	p14 = Point(x - 6 * k, y + 6 * k)
	p13 = Point(x - 2 * k, y + 8 * k)
	p12 = Point(x - 2 * k, y + 10 * k)
	p11 = Point(x - 4 * k, y + 13 * k)
	p10 = Point(x - 3 * k, y + 14 * k)
	r = Polygon(p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16)
	r.setFill('black')
	r.setOutline('black')
	r.draw(win)


def shu(win):
	DrawShu(420, 300, win, 2)
	DrawShu(450, 320, win, 4)
	DrawShu(130, 330, win, 3)


def DrawShu(x, y, win, size):
	o1 = Oval(Point(x - 3 * size, y + 16 * size), Point(x + 3 * size, y + 18 * size))
	o1.setFill('grey')
	o1.draw(win)
	r = Rectangle(Point(x - 2 * size, y), Point(x + 2 * size, y + 17 * size))
	r.setFill('brown')
	r.setOutline('brown')
	r.draw(win)
	S = [[3, 4, 4], [4, -3, 3], [5, 2, 3], [0, -4, 4], [-3, 5, 3], [-4, -3, 3], [-5, 2, 3], [-3, 0, 3], [0, 0, 3]]
	for i in S:
		c = Circle(Point(x + size * i[0], y + size * i[1]), size * i[2])
		c.setOutline('green')
		c.setFill('green')
		c.draw(win)


def men(win):
	Mzuo(win)
	Myou(win)
	Mzhu(win)
	Mheng(win)


def Mzuo(win):
	for i in range(250):
		c = Circle(Point(i, 200 + round(5.0 / 490 * (i - 180) ** 2)), 6)
		c.setOutline('papayawhip')
		c.setFill('papayawhip')
		c.draw(win)


def Mheng(win):
	for i in range(250, 300):
		c = Circle(Point(i, 250 - round(1.0 / 10 * (i - 250))), 4)
		c.setOutline('papayawhip')
		c.setFill('papayawhip')
		c.draw(win)
	for i in range(270, 290):
		c = Circle(Point(i, 380 + round(1.0 / 20 * (i - 250))), 4)
		c.setOutline('papayawhip')
		c.setFill('papayawhip')
		c.draw(win)


def Myou(win):
	for i in range(300):
		c = Circle(Point(300 + i, 180 + round(6.0 / 810 * (i - 90) ** 2)), 6)
		c.setOutline('papayawhip')
		c.setFill('papayawhip')
		c.draw(win)


def Mzhu(win):
	for i in range(7):
		for j in range(3 + int(round((250 - 10.0 / 6 * i))), 380):
			c = Circle(Point((250 + 50.0 / 6 * i) + (280 - (250 + 50.0 / 6 * i)) / (380 - (250 - 10.0 / 6 * i)) * (
				j - (250 - 10.0 / 6 * i)), j), 1)
			c.setOutline('white')
			c.setFill('red')
			c.draw(win)


def lou(win):
	DrawLou(460, 300, 4, win, 'darkred')
	DrawLou(490, 300, 5, win, 'darkred')
	DrawLou(530, 280, 7, win, 'darkred')
	DrawLou(100, 300, 4, win, 'burlywood')
	DrawLou(60, 300, 5, win, 'burlywood')
	DrawLou(0, 280, 7, win, 'burlywood')


def DrawLou(x, y, size, win, color):
	r = Rectangle(Point(x, y - 4 * size), Point(x + 6 * size, y))
	r.setFill(color)
	r.draw(win)
	r = Rectangle(Point(x, y), Point(x + 10 * size, y + 18 * size))
	r.setFill(color)
	r.draw(win)
	r = Rectangle(Point(x + 2 * size, y + 2 * size), Point(x + 8 * size, y + 4 * size))
	r.setFill('black')
	r.draw(win)
	r = Rectangle(Point(x + 2 * size, y + 6 * size), Point(x + 8 * size, y + 8 * size))
	r.setFill('black')
	r.draw(win)
	r = Rectangle(Point(x + 2 * size, y + 10 * size), Point(x + 8 * size, y + 12 * size))
	r.setFill('black')
	r.draw(win)
	r = Rectangle(Point(x + 2 * size, y + 14 * size), Point(x + 8 * size, y + 16 * size))
	r.setFill('black')
	r.draw(win)


def qi(win):
	DrawQi(200, 160, win, 5)
	DrawGan(200, 160, win, 170)
	DrawTai(200, 160, win, 170)


def DrawGan(x, y, win, lenth):
	p1 = Point(x - 2, y)
	p2 = Point(x, y + lenth)
	r = Rectangle(p1, p2)
	r.setFill('white')
	r.draw(win)


def DrawTai(x, y, win, lenth):
	p1 = Point(x - 15, y + lenth)
	p2 = Point(x + 15, y + lenth + 4)
	r = Rectangle(p1, p2)
	r.setOutline('brown')
	r.setFill('brown')
	r.draw(win)


def DrawQi(x, y, win, k):
	p0 = Point(x, y)
	p1 = Point(x + 1 * k, y - 1 * k)
	p2 = Point(x + 3 * k, y - 2 * k)
	p3 = Point(x + 5 * k, y - 1 * k)
	p4 = Point(x + 8 * k, y)
	p5 = Point(x + 8 * k, y + 6 * k)
	p6 = Point(x + 5 * k, y - 1 * k + 6 * k)
	p7 = Point(x + 3 * k, y - 2 * k + 6 * k)
	p8 = Point(x + 1 * k, y - 1 * k + 6 * k)
	p9 = Point(x, y + 6 * k)
	qi = Polygon(p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)
	qi.setFill('red')
	qi.setOutline('red')
	qi.draw(win)


def logo(win):
	o = Circle(Point(275, 240), 18)
	o.setOutline('blue')
	o.setFill('blue')
	o.draw(win)


main()
