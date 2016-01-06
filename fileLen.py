#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
path = os.path.join(os.getcwd(), "resource")
def oneLineFileMake():
    with open(os.path.join(path, "test.rtf"), "w") as one:
        one.write("This file only has one line.")

def oneLineFileget():
    with open(os.path.join(path, "test.rtf"), "r") as one:
        if sum(1 for x in one) == 1:
            print(one.readline())

def oneLineFileget2():
    with open(os.path.join(path, "test.rtf"), "r") as one:
        if sum(1 for x in one) == 1:
            print("Oh, I'm reall here.")
            one.seek(0)
            print(one.readline())

if __name__ == '__main__':
    oneLineFileMake()
    oneLineFileget()
    # oneLineFileget2()
