#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def printIDofSameValue(a, b):
    if a != b:
        print("Not same.")
    if id(a) != id(b):
        print("%s: id%s, %s: id%s" % (a, id(a), b, id(b)))
    else:
        print("%s: id%s" % (a, id(a)))

def testIDs():
    a, b = 1, 1
    printIDofSameValue(a,b)       
    a, b = -6, -6
    printIDofSameValue(a,b)
    k = -7 
    a, b = k, k
    printIDofSameValue(a,b)
    
    a = list(range(-6, 258))
    b = list(range(-6, 258))
    printIDofSameValue(a[0],b[0])
    
    for i in range(len(a)):        # [-5, 256]
        if id(a[i]) != id(b[i]):
            print("%s: id%s, %s: id%s" % (a[i], id(a[i]), b[i], id(b[i])))

def changeAtoBWhenSmall(a, b):
    import ctypes
    ivalOffset = ctypes.sizeof(ctypes.c_size_t) + ctypes.sizeof(ctypes.c_voidp)
    ival = ctypes.c_int.from_address(id(a) + ivalOffset)
    ival.value = b

if __name__ == '__main__':
    # testIDs()
    # import ctypes
    # value = 2
    # ivalOffset = ctypes.sizeof(ctypes.c_size_t) + ctypes.sizeof(ctypes.c_voidp)
    # ival = ctypes.c_int.from_address(id(value) + ivalOffset)
    # ival.value = 3
    x = 1 + 1
    changeAtoBWhenSmall(2, 4)
    print(x)