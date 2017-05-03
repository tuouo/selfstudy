#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/5/3


class A(object):
    def __init__(self):
        print("In A")
        super(A, self).__init__()
        print("ooooooooooooo A")

    def go(self):
        print("A")

    @staticmethod
    def go_static():
        print("A staticmethod")

    @classmethod
    def go_class(cls):
        print("A classmethod")


class B(object):
    def __init__(self):
        print("In B")
        super(B, self).__init__()  # if not add, trace will stop here
        print("ooooooooooooo B")


class C(A):
    def __init__(self):
        print("In C")
        super(C, self).__init__()
        print("ooooooooooooo C")

    def go(self):
        print("C")

    @staticmethod
    def go_static():
        print("C staticmethod")

    @classmethod
    def go_class(cls):
        print("C classmethod")


class D(A):
    def __init__(self):
        print("In D")
        super(D, self).__init__()
        print("ooooooooooooo D")


class E(B, C):
    def __init__(self):
        print("In E")
        super(E, self).__init__()
        print("ooooooooooooo E")


class F(E, D):
    def __init__(self):
        print("In F")
        super(F, self).__init__()
        print("ooooooooooooo F")


class G(D, C):
    def __init__(self):
        print("In G")
        super(G, self).__init__()
        print("ooooooooooooo G")


if __name__ == '__main__':
    # g = G()
    # g.go()
    # g.go_class()
    # g.go_static()
    f = F()
