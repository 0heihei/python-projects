# Based on perceptual hash algorithms

from PIL import Image
from functools import reduce
import imagehash
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal
from operator import lt


class Hash:
    def __init__(self):
        self.img = Image.open('test.jpg').convert('L')

    def aHash(self):
        """
            Average Hash or Mean Hash
            :param im:
            :return:
            """
        img = self.img.resize((8, 8), Image.LANCZOS)
        avg = reduce(lambda x, y: x + y, img.getdata()) / 64
        tmp = []
        for i, j in enumerate(img.getdata()):
            tmp.append(0 if j < avg else 1)
        value = (''.join(map(str, tmp)))
        print(value)

    def pHash(self):
        """
        Perceptive Hash
        :param im:
        :return:
        """


    def dHash(self):
        """
        Difference hash
        :param im:
        :return:
        """

        difference = self.difference()
        # 转化为16进制(每个差值为一个bit,每8bit转为一个16进制)
        decimal_value = 0
        hash_string = ""
        for index, value in enumerate(difference):
            if value:  # value为0, 不用计算, 程序优化
                decimal_value += value * (2 ** (index % 8))
            if index % 8 == 7:  # 每8位的结束
                hash_string += str(hex(decimal_value)[2:].rjust(2, "0"))  # 不足2位以0填充。0xf=>0x0f
                decimal_value = 0
        return hash_string

    def difference(self):
        """
        *Private method*
        计算image的像素差值
        :param image: PIL.Image
        :return: 差值数组。0、1组成
        """
        resize_width = 9
        resize_height = 8
        # 1. resize to (9,8)
        smaller_image = self.img.resize((resize_width, resize_height))
        # 2. 灰度化 Grayscale
        grayscale_image = smaller_image.convert("L")
        # 3. 比较相邻像素
        pixels = list(grayscale_image.getdata())
        difference = []
        for row in range(resize_height):
            row_start_index = row * resize_width
            for col in range(resize_width - 1):
                left_pixel_index = row_start_index + col
                difference.append(pixels[left_pixel_index] > pixels[left_pixel_index + 1])
        return difference

    def hamming_distance(self, hash1, hash2):
        """
        :param hash1: string
        :param hash2:
        :return:
        """
        return sum(i!=j for i,j in zip(hash1,hash2))


#getHash = Hash()
#getHash.aHash()


#img=Image.open('test.jpg')
#print(imagehash.average_hash(img))
