#coding=utf-8

import cv2 as cv
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import random


class pngproducer:
    def __init__(self):
        self.img = cv.imread('images/background.jpg')
        self.symble = ['，','。','：','(',')','/','.','、']  # 中文标点
        self.alpho = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
        self.digtal = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

        self.file = open("homework.txt", "r", encoding="utf8")
        self.text = self.file.readlines()
        print("读取文件成功")
        self.y_interval = 55  # 汉字间距
        self.x_interval = 45  # 汉字行距
        self.x_begin = 45  # 汉字坐对其
        self.y_begin = 400 # 汉字最高点
        self.x = self.x_begin  # 打印字体位置
        self.y = self.y_begin
        self.pages = 0  # 页数
        # 图片转换（cv2 -> pil）
        self.cv2img = cv.cvtColor(self.img, cv.COLOR_BGR2RGB)
        self.pilimg = Image.fromarray(self.cv2img)
        # 在图片上添加文字（支持中文）
        self.draw = ImageDraw.Draw(self.pilimg)  # 画板
        self.font = ImageFont.truetype("迎风自由手书体.ttf", 50, encoding="utf-8")  #手写字体
        self.offset_range = 10  # 单字偏移范围
        self.fontcolor = (255, 255, 255)  # 字体颜色
        # self.rownum = 24  # 一行的字数
        self.x_max = 1550  # 右对其
        self.y_max = 2300  # 最多底y
        self.i = 0

    def run(self):
        for strs in self.text:
            print(strs)
            for char in strs:  # 处理每个字
                if(self.x < self.x_max and self.y < self.y_max):
                    self.word(char)
                elif(self.x >= self.x_max and (self.y+self.y_interval) < self.y_max):  # 换行
                    self.x = self.x_begin
                    self.y += self.y_interval
                    self.word(char)
                elif(self.y >= self.y_max):  # 换页
                    self.x = self.x_begin
                    self.y = self.y_begin
                    self.finish()

                    self.word(char)

            self.y += self.y_interval
            self.y += self.y_interval
            self.x = self.x_begin

        self.finish()
    def finish(self):
        print("一页写完,保存图片{}.jpg".format(self.pages))
        # 图片转换（pil -> cv2）
        self.cv2img2 = cv.cvtColor(np.array(self.pilimg), cv.COLOR_RGB2BGR)
        # 保存图片到当前目录
        cv.imwrite(str(self.pages) + '.jpg', self.cv2img2)
        # 重新画图
        self.pilimg = Image.fromarray(self.cv2img)
        self.draw = ImageDraw.Draw(self.pilimg)
        self.pages += 1

    def word(self, char):
        print('char:  ',char)
        if(char in self.alpho):
            self.writeEnglish(char)

        elif(char.isdigit()):
            self.writeEnglish(char)

        elif(char in self.symble):
            self.writeEnglish(char)

        else:
            self.writeChinese(char)


    def writeChinese(self,char):
        print('汉字:  ',char)
        self.offset_x = random.randint(0, self.offset_range)
        self.offset_y = random.randint(0, self.offset_range)
        self.draw.text((self.x + self.offset_x, self.y + self.offset_y), char, self.fontcolor, font=self.font)
        self.x += self.x_interval

    def writeEnglish(self, char):
        print('字符:  ', char)
        self.offset_x = random.randint(0, 3)
        self.offset_y = random.randint(0, self.offset_range)
        x_reduce = 10
        self.draw.text((self.x + self.offset_x - x_reduce, self.y + self.offset_y), char, self.fontcolor, font=self.font)
        self.x += self.x_interval
        self.x -= x_reduce
        self.x -= 15

if(__name__ == '__main__'):
    hero = pngproducer()
    hero.run()

