#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image
# im = Image.open('123.png')
# print(im.format, im.size, im.mode)
# im.thumbnail((200, 100))
# im.save('12321.jpg', 'JPEG')

# import os 
# path = os.path.join(os.path.abspath('.'), 'resource')
# print(path) 
# from PIL import ImageFilter
# im = Image.open(os.path.join(path, '123.png'))
# w, h = im.size
# print('image size: %s X %s' % (w, h) )
# im2 = im.filter(ImageFilter.BLUR)
# im2.save(os.path.join(path, '123bule.jpg'), 'jpeg')

from PIL import ImageDraw, ImageFont, ImageFilter
import random, os 
def random_char():
    return chr(random.randint(65,90))
	
def random_color():
    return (random.randint(64,255), random.randint(64,255), random.randint(64,255))

def random_color2():
    return (random.randint(32,127), random.randint(32,127), random.randint(32,127))

width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255,255,255))
path = os.path.join('C:', 'soft', 'Inconsolata', 'Inconsolata.otf')
font = ImageFont.truetype(path, 36)
draw = ImageDraw.Draw(image)
for x in range(width):
    for y in range(height):
        draw.point((x,y), fill = random_color())
for i in range(4):
    draw.text((60 * i + 10, 10), random_char(), font = font, fill = random_color2())
image = image.filter(ImageFilter.BLUR)
path = os.path.join(os.path.abspath('.'), 'resource', 'random.jpg')
image.save(path, 'jpeg')
