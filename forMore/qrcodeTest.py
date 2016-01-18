#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import qrcode
"""
If This file name qrcode.py which has the same name of the module of qrcode.
Then import qrcode means import this file, not the module.
"""

data = "https://github.com/tuouo/games/blob/master/nonogram/nonogram.py"
# im = qrcode.make(data)
# im.save("oooo.png")
# # im.show()
qr = qrcode.QRCode(
       version = 1,
       error_correction = qrcode.constants.ERROR_CORRECT_L,
       box_size = 20,
       border = 4,
    )
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image()
img.save("1L20.png")
# img.save("0L20.png")
# # img.show()