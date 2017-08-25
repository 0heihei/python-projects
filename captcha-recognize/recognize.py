from PIL import Image


def x_segment(bin_img):
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
            seg_list.extend([x0[i - 1], x0[i]])
    seg_list.append(x0[-1])
    print(x0)
    print(seg_list)
    # 分割图像
    for i in range(int(len(seg_list) / 2)):
        print([seg_list[i] * 2, 0, seg_list[i * 2 + 1], height])
        seg_img = bin_img.crop([seg_list[i] * 2, 0, seg_list[i * 2 + 1], height])
        seg_img.show()


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


def recognize(img):
    """
    暂时没想好具体的识别比对算法
    :param img:
    :return:
    """
    pass


img = Image.open('./imgs/0.jpg').convert('L')
bin_img = b_process(img, 200)
x_segment(bin_img)
