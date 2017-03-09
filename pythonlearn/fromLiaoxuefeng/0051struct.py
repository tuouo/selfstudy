#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import struct
print(struct.pack('>I', 10240099))

testByte = b'\xf0\xf0\xf0\xf0\x80\x80'
print(struct.unpack('>I', b'\xf0\xf0\xf0\xf0'))
print(struct.unpack('>H', b'\x80\x80'))
print(struct.unpack('>IH', testByte))

def infoBMP(dir):
    with open(dir, 'rb') as f:
        s = f.read(30)
        if len(s) >= 30:
            print(s)
            info = struct.unpack('<ccIIIIIIHH', s)
            print(info)
            if (info[0] == b'B' and info[1] == b'M'
               and info[3] == 0 and info[8] == 1):
                    return (info[2], info[9])
            else:
                    print("not BMP")
				
info = infoBMP(r'.\123.bmp')
if info:
    print(info)
else:
    print('something wrong')