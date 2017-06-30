# -*- coding: utf-8 -*-
from Tkinter import *
from PIL import Image

a = input("请输入图片名称 PS：从1,2,3中选择")  # 选择要输入的文件
if a != 1 and a != 2 and a != 3 and a != 4:
	print("请重新输入！")
img = Image.open(str(a) + ".jpg")  # 打开图片文件
img.save("test.jpg")  # 另存为
img = img.convert("L")  # 将图片灰度化
# img.show()
imgSize = img.size
img_array = img.load()
root = Tk()
if a == 1:
	print '已经另存为test.jpg'
elif a == 2:
	root.title('庙门狮子（像素版）')
elif a == 3:
	root.title('交大思源湖畔（像素版）')
else:
	root.title('女神（像素版）')
width, height = imgSize[0] * 4, imgSize[1] * 4
canvas = Canvas(root, width=width, height=height)  # 创建画布
count = 0
for i in range(imgSize[0]):
	for j in range(imgSize[1]):
		# print img_array[i,j]
		if img_array[i, j] <= 30:  # 对于不同灰度进行颜色划分，共九种不同的颜色
			a = "black"
		# print a
		elif img_array[i, j] <= 60:
			a = "dimgray"
		# print a
		elif img_array[i, j] <= 90:
			a = "gray"
		# print a
		elif img_array[i, j] <= 120:
			a = "darkgray"
		# print a
		elif img_array[i, j] <= 150:
			a = "silver"
		# print a
		elif img_array[i, j] <= 180:
			a = "lightgray"
		# print a
		elif img_array[i, j] <= 210:
			a = "gainsboro"
		# print a
		elif img_array[i, j] <= 235:
			a = "whitesmoke"
		# print a
		else:
			a = "white"
		# print a
		canvas.create_oval(i * 4, j * 4, (i + 1) * 4, (j + 1) * 4, fill=a)  # 画出某个像素点
	# count += 1 #用于测试
	# print count #用于测试
canvas.pack()
root.mainloop()
