#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image
im = Image.open('123.png')
print(im.format, im.size, im.mode)
im.thumbnail((200, 100))
im.save('12321.jpg', 'JPEG')
