#!/usr/bin/env python
# coding:utf-8
# Created by Hisen on 2015/4/14

import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import time
font = ImageFont.truetype("statics/font/ARLRDBD.TTF",40)

def addwatermark(name):
    print 'add'
    imageFile = '%s.jpg'%name
    print imageFile
    im1=Image.open('statics/livepics/%s'%imageFile)

    date =time.strftime('%Y_%m_%d %H:%M:%S')
    draw = ImageDraw.Draw(im1)
    draw.text((180, 510),date,(255,255,0),font)
    draw = ImageDraw.Draw(im1)
    im1.save('statics/livepics/%s'%imageFile)
    return True