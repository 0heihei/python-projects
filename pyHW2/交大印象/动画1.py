# -*- coding: utf8 -*-
from math import *
from graphics import *

win = GraphWin("SJTU", 650, 550)


def line_1(win):
	y = 0
	while y <= 340:
		Line(Point(500, 500 - y - 7), Point(520, 500 - y - 7)).draw(win)
		if y % 80 == 20:
			y = y + 60
		else:
			y = y + 20


def line_2(win):
	y = 0
	while y <= 340:
		Line(Point(520, 500 - y - 7), Point(570, 500 - (y + 30 - 7))).draw(win)
		if y % 80 == 20:
			y = y + 60
		else:
			y = y + 20


def line_3(win):
	y = 0
	while y <= 340:
		Line(Point(570, 500 - (y + 30 - 7)), Point(590, 500 - (y + 30 - 7))).draw(win)
		if y % 80 == 20:
			y = y + 60
		else:
			y = y + 20


def line_4(win):
	y = 0
	while y <= 340:
		Line(Point(500, 500 - (y + 20) - 7), Point(500, 500 - (y + 20) - 7 + 20)).draw(win)
		y = y + 80


def line_5(win):
	y = 0
	while y <= 340:
		Line(Point(590, 500 - (y + 30 - 7)), Point(590, 500 - (y + 30 - 7) - 20)).draw(win)
		y = y + 80


def line_6(win):
	Line(Point(260, 100), Point(570, 100)).draw(win)
	Line(Point(300, 70), Point(610, 70)).draw(win)
	Line(Point(570, 477), Point(570, 510)).draw(win)
	y = 0
	while y <= 260:
		Line(Point(570, 500 - y - 43), Point(570, 500 - (y + 60) - 43)).draw(win)
		y = y + 80
	Line(Point(570, 100), Point(570, 140)).draw(win)
	Line(Point(610, 70), Point(610, 480)).draw(win)
	Line(Point(570, 100), Point(610, 70)).draw(win)
	Line(Point(570, 510), Point(610, 480)).draw(win)


def line_7(win):
	y = 0
	while y <= 340:
		Line(Point(320, 500 - (y + 5)), Point(320, 500 - (y + 65))).draw(win)
		Line(Point(390, 500 - (y + 5)), Point(390, 500 - (y + 65))).draw(win)
		Line(Point(460, 500 - (y + 5)), Point(460, 500 - (y + 65))).draw(win)
		y = y + 80


def line_8(win):
	y = 0
	while y <= 340:
		Line(Point(320, 500 - (y + 5)), Point(460, 500 - (y + 5))).draw(win)
		Line(Point(320, 500 - (y + 5) - 60), Point(460, 500 - (y + 5) - 60)).draw(win)
		y = y + 80


def line_9(win):
	Line(Point(0, 510), Point(650, 510)).draw(win)


def tx_1(win):
	for a in range(20, 380):
		Point(a, int(520 - abs(200 * sin((a - 20) * pi / 180.0)))).draw(win)
		Point(a, int(520 - abs(150 * sin((a - 20) * pi / 180.0))) - 20).draw(win)


def text(win):
	for i in range(73):
		Point(50 - int(20 * sin((i - 11) * pi / 26.0)), i + 90).draw(win)
	for i in range(45):
		Point(i + 80, 90).draw(win)
	for i in range(65):
		Point(105, i + 90).draw(win)
	for i in range(12):
		Point(i + 93, 5 * sin((i + 24) * pi / 12) + 155).draw(win)
	for i in range(50):
		Point(i + 135, 90).draw(win)
	for i in range(73):
		Point(160, i + 90).draw(win)
	for i in range(63):
		Point(194, i + 90).draw(win)
		Point(230, i + 90).draw(win)
	for i in range(37):
		Point(i + 193, 10 * sin((i) * pi / 35) + 154).draw(win)


def main(win):
	line_1(win)
	line_2(win)
	line_3(win)
	line_4(win)
	line_5(win)
	line_6(win)
	line_7(win)
	line_8(win)
	line_9(win)
	tx_1(win)
	text(win)
	win.mainloop()


main(win)
