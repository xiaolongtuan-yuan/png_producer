#coding=utf-8
import yaml
import cv2 as cv
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import random

with open('config/picture.yaml') as configs:
    config = yaml.load(configs, Loader=yaml.FullLoader)

    # 当前目录读取一张图片
    img = cv.imread('images/'+config['background']+'.jpg')

    file = open("homework.txt", "r", encoding="utf8")
    text = file.readlines()
    print("读取文件成功")
    y_interval = config['y_interval']
    x_interval = config['x_interval']
    x_begin = config['x_begin']
    y_begin = config['y_begin']
    fontcolor = tuple(config['fontcolor'])
    rownum = config['rownum']
    y_max = config['y_max']
    x = x_begin  # 打印字体位置
    y = y_begin
    pages = 0
    offset_range = 10
    i = 0
    font = ImageFont.truetype("迎风自由手书体.ttf", 50, encoding="utf-8")

    # 图片转换（cv2 -> pil）
    cv2img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    pilimg = Image.fromarray(cv2img)

    # 在图片上添加文字（支持中文）
    draw = ImageDraw.Draw(pilimg)


    for strs in text:
        if y >= y_max:
            print("一页写完,保存图片{}.jpg".format(pages))
            # 图片转换（pil -> cv2）
            cv2img2 = cv.cvtColor(np.array(pilimg), cv.COLOR_RGB2BGR)
            # 保存图片到当前目录
            cv.imwrite(str(pages)+'.jpg', cv2img2)
            # 重新画图
            pilimg = Image.fromarray(cv2img)
            draw = ImageDraw.Draw(pilimg)
            pages += 1
            x = x_begin
            y = y_begin

            for c in strs:
                offset_x = random.randint(0, offset_range)
                offset_y = random.randint(0, offset_range)
                if i >= rownum:  # 换行
                    i = 0
                    x = x_begin
                    y = y + y_interval
                    draw.text((x + offset_x, y + offset_y), c, fontcolor, font=font)
                    x += x_interval
                    i += 1
                else:
                    draw.text((x + offset_x, y + offset_y), c, fontcolor, font=font)
                    x += x_interval
                    i += 1
            x = x_begin
            y += y_interval
        else:
            for c in strs:
                offset_x = random.randint(0, offset_range)
                offset_y = random.randint(0, offset_range)
                if i >= rownum: # 换行
                    i = 0
                    x = x_begin
                    y = y + y_interval
                    draw.text((x + offset_x, y + offset_y), c, fontcolor, font=font)
                    x += x_interval
                    i += 1
                else:
                    draw.text((x+offset_x, y+offset_y), c, fontcolor, font=font)
                    x += x_interval
                    i += 1
            print(strs)
            y += y_interval
            i = 0
            x = x_begin
    # 图片转换（pil -> cv2）
    cv2img2 = cv.cvtColor(np.array(pilimg), cv.COLOR_RGB2BGR)
    # 保存图片到当前目录
    cv.imwrite(str(pages)+'.jpg', cv2img2)

    file.close()


# # 显示图片
# cv.imshow("show Chloe2", cv2img2)
# cv.waitKey(0)

# saveImagePath = ‘E:/ScreenTestImages/’
# colorRed = [0,0,255]
# colorGreen = [0,255,0]
# colorBlue = [255,0,0]
# colorWhite = [255,255,255]
# colorBlack = [0,0,0]
# colorAqua = [255,255,0]
# colorFuchsia = [255,0,255]
# colorYellow = [0,255,255]
# stardardColors = [colorBlue,colorGreen,colorAqua,colorRed,colorFuchsia,colorYellow,colorWhite]
# def createImg(depth=3):
#     return cv.CreateImage((800,480),8,depth)
# def saveImageFile(typeName,img):
#     filename = saveImagePath + typeName + ‘.png’
#     cv.SaveImage(filename,img)
#     print typeName+’.png’,’\t\t…\tok’
# def createOneColorImage(color):
#     img = createImg()
#     cv.Set(img,color)
#     return img
# def create64GrayImage():
#     img = createImg(1)
#     cv.SetZero(img)
#     for xPos in range(0,64):
#     cv.SetImageROI(img,(int(12.5xPos),0,800,480))
#     cv.Set(img,xPos255/63)
#     cv.ResetImageROI(img)
#     return img
# def createCheckBoardPattern(isReserved=False):
#     img = createImg(1)
#     boolColor = True
#     numsX = 4
#     numsY = 4
#     pixsX = 800/numsX
#     pixsY = 480/numsY
#     for x in range(0,numsX):
#     for y in range(0,numsY):
#     cv.SetImageROI(img,(xpixsX,ypixsY,(x+1)pixsX,(y+1)pixsY))
#     boolColor = not (x%2) ^ (y%2) ^ isReserved
#     cv.Set(img,255boolColor)
#     cv.ResetImageROI(img)
#     return img
# def createStardardImage():
#     img = createImg()
#     pixs = 800./7
#     for i in range(0,7):
#     cv.SetImageROI(img,(int(ipixs),0,int(i*pixs+pixs),480))
#     cv.Set(img,stardardColors[i])
#     cv.ResetImageROI(img)
#     return img
# if name == ‘main’:
#     print ‘Start Gen Test Screen Files …’
#     saveImageFile(‘red’,createOneColorImage(colorRed))
#     saveImageFile(‘green’,createOneColorImage(colorGreen))
#     saveImageFile(‘blue’,createOneColorImage(colorBlue))
#     saveImageFile(‘white’,createOneColorImage(colorWhite))
#     saveImageFile(‘black’,createOneColorImage(colorBlack))
#     saveImageFile(‘64gray’,create64GrayImage())
#     saveImageFile(‘checkboard Pattern’,createCheckBoardPattern())
#     saveImageFile(‘checkboard Pattern(inverted)’,createCheckBoardPattern(True))
#     saveImageFile(‘standard’,createStardardImage())
#     print ‘Generate Success!’
