"""
将原始图像进行分割，并进行标记（放到对应的文件夹中）。
先前打算分割之后人工进行归类，可是数目实在太大根本弄不过来。遂打算采用pytesseract
由于pytesseract不能识别分割后的单个字母，索性让其识别整个验证码，再将验证码进行分割归类。如此甚好！
最后只需要人为地进行一些剔选就得到了很好的训练样本
input: ./raws_samples
output:./train_samples
"""

import os
from PIL import Image
from pytesseract import image_to_string

"""
#先建立好归类文件夹
if os.path.exists('training_samples'):
    pass
else:
    os.mkdir('training_samples')
os.chdir('./training_samples')
for i in 'abcdefghijklmnopqrstuvwxyz1234567890':
    if os.path.exists(i):
        pass
    else:
        os.mkdir(i)
"""


def b_process(img, threshold):
    """
    :param img:A gray-image,eg:img=Image.open(image).convert("L")
    :param threshold:
    :return:
    """
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    bin_img = img.point(table, '1')
    return bin_img


def x_segment(bin_img, img_name, margin=3):
    """
    :param bin_img:A binary-processed image.
    :return: segmented raws
    """
    width, height = bin_img.size
    pix = bin_img.load()
    # 列表保存像素累加值大于0的列
    x0 = []
    for x in range(width):
        pixel = 0
        for y in range(height):
            if pix[x, y] == 0:
                pixel += 1
        if pixel > 0:
            x0.append(x)
    # 找出边界
    seg_list = []
    seg_list.append(0)
    for i in range(1, len(x0)):
        if x0[i] - x0[i - 1] > 1:
            seg_list.extend([x0[i - 1] + margin, x0[i] - margin])
    seg_list.append(x0[-1])
    # 分割图像并归入对应的文件夹中
    string = image_to_string(bin_img)
    try:  # 识别到的字符不在我的归类范围（并未预先建立相应字符的文件夹）
        for i in range(int(len(seg_list) / 2)):
            if len(string) != len(seg_list) / 2:  # 万一 实际识别到的字符数目和分割的不同
                continue
            seg_img = bin_img.crop([seg_list[i] * 2, 0, seg_list[i * 2 + 1], height])
            if seg_img.size[0] == 0 or seg_img.size[1] == 0:
                continue
            seg_img.save('../training_samples/' + string[i] + '/' + str(i) + img_name)
    except:
        pass


os.chdir('./raws_samples')
imgs = os.listdir('.')
for pic in imgs:
    img = Image.open(pic).convert('L')
    bin_img = b_process(img, 200)
    x_segment(bin_img, pic)
