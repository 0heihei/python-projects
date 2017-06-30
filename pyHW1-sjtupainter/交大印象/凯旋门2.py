# -*- coding: utf-8 -*-

from graphics import *

win = GraphWin("凯旋门2", 600, 400)
win.setCoords(0, 0, 600, 400)

# 画拱上边及侧边直线，左右柱上端侧面斜短线
up = Line(Point(236, 300), Point(394, 300))
left1 = Line(Point(236, 300), Point(236, 240))
left2 = Line(Point(230, 300), Point(236, 294))
right1 = Line(Point(394, 300), Point(394, 240))
right2 = Line(Point(394, 300), Point(400, 294))
up.draw(win)
left1.draw(win)
right1.draw(win)
left2.draw(win)
right2.draw(win)

# 画左右柱正面矩形

leftrect = Rectangle(Point(200, 0), Point(230, 300))
rightrect = Rectangle(Point(400, 0), Point(430, 300))
leftrect.draw(win)
rightrect.draw(win)

# 画左右柱侧面底线
lbehind = Line(Point(230, 0), Point(280, 50))
rbehind = Line(Point(430, 0), Point(480, 50))
lbehind.draw(win)
rbehind.draw(win)

# 画左右柱侧面其他部分
rbehind1 = Line(Point(430, 300), Point(480, 270))
rbehind2 = Line(Point(480, 50), Point(480, 270))
lbehind1 = Line(Point(280, 50), Point(280, 224))
rbehind1.draw(win)
rbehind2.draw(win)
lbehind1.draw(win)

# 画拱中间直线及两边短线
up2 = Line(Point(280, 240), Point(350, 240))
upleft = Line(Point(230, 240), Point(236, 240))
upright = Line(Point(394, 240), Point(400, 240))
up2.draw(win)
upleft.draw(win)
upright.draw(win)

# 画拱左边折线部分
left01 = Line(Point(230, 200), Point(240, 200))
left02 = Line(Point(240, 200), Point(240, 210))
left03 = Line(Point(240, 210), Point(270, 230))
left04 = Line(Point(270, 230), Point(280, 230))
left05 = Line(Point(280, 230), Point(280, 240))
left01.draw(win)
left02.draw(win)
left03.draw(win)
left04.draw(win)
left05.draw(win)

# 画拱右边折线部分
right01 = Line(Point(350, 240), Point(350, 230))
right02 = Line(Point(350, 230), Point(360, 230))
right03 = Line(Point(360, 230), Point(390, 210))
right04 = Line(Point(390, 210), Point(390, 200))
right05 = Line(Point(390, 200), Point(400, 200))
right01.draw(win)
right02.draw(win)
right03.draw(win)
right04.draw(win)
right05.draw(win)

# 画大六边形
p1, p2, p3 = Point(295, 290), Point(265, 270), Point(295, 250)
p4, p5, p6 = Point(335, 250), Point(365, 270), Point(335, 290)
poly1 = Polygon(p1, p2, p3, p4, p5, p6)
poly1.draw(win)

# 画小六边形
q1, q2, q3 = Point(301, 284), Point(279, 270), Point(301, 256)
q4, q5, q6 = Point(329, 256), Point(351, 270), Point(329, 284)
poly2 = Polygon(q1, q2, q3, q4, q5, q6)
poly2.draw(win)

# 画拱后面阴影
behind1 = Line(Point(230, 200), Point(236, 194))
behind2 = Line(Point(236, 194), Point(246, 194))
behind3 = Line(Point(246, 194), Point(246, 204))
behind4 = Line(Point(246, 204), Point(276, 224))
behind5 = Line(Point(276, 224), Point(286, 224))
behind6 = Line(Point(286, 224), Point(286, 234))
behind7 = Line(Point(286, 234), Point(350, 234))
behind8 = Line(Point(356, 224), Point(366, 224))
behind9 = Line(Point(396, 194), Point(400, 194))
behind1.draw(win)
behind2.draw(win)
behind3.draw(win)
behind4.draw(win)
behind5.draw(win)
behind6.draw(win)
behind7.draw(win)
behind8.draw(win)
behind9.draw(win)

# 画连接拱正面和后面阴影的斜短线
link1 = Line(Point(246, 194), Point(240, 200))
link2 = Line(Point(246, 204), Point(240, 210))
link3 = Line(Point(276, 224), Point(270, 230))
link4 = Line(Point(286, 224), Point(280, 230))
link5 = Line(Point(286, 234), Point(280, 240))
link6 = Line(Point(350, 230), Point(356, 224))
link7 = Line(Point(390, 200), Point(396, 194))
link1.draw(win)
link2.draw(win)
link3.draw(win)
link4.draw(win)
link5.draw(win)
link6.draw(win)
link7.draw(win)

# 画石碑以及下面基石
block1 = Rectangle(Point(290, 27), Point(380, 55))
block1.draw(win)
block1 = Rectangle(Point(280, 20), Point(390, 25))
block1.draw(win)
blockb1 = Line(Point(292, 57), Point(382, 57))
blockb2 = Line(Point(382, 27), Point(382, 57))
blockb3 = Line(Point(282, 27), Point(392, 27))
blockb4 = Line(Point(392, 22), Point(392, 27))
bline1 = Line(Point(290, 55), Point(290, 57))
bline2 = Line(Point(380, 55), Point(382, 57))
bline3 = Line(Point(280, 25), Point(282, 27))
bline4 = Line(Point(390, 25), Point(392, 27))
bline5 = Line(Point(390, 20), Point(392, 22))
blockb1.draw(win)
blockb2.draw(win)
blockb3.draw(win)
blockb4.draw(win)
bline1.draw(win)
bline2.draw(win)
bline3.draw(win)
bline4.draw(win)
bline5.draw(win)

# 石碑上刻字：     交通大学
SJTU = Text(Point(335, 41), '交通大学')
SJTU.draw(win)

win.mainloop()
