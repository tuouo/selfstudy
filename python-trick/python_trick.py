#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/4/12
from functools import wraps


def show_method_name(fuc):
    @wraps(fuc)
    def wrapper():
        print("\n\t", fuc.__name__)
        fuc()
    return wrapper


class EssentialTipsAndTricks:
    """
    http://www.techbeamers.com/essential-python-tips-tricks-programmers/
    """

    @staticmethod
    # @show_method_name
    def print_file_path_of_imported_variables():
        import sys
        import os
        print("Path of sys:", sys)
        print("Path of os:", os)

    @staticmethod
    def dictionary_set_comprehensions():
        test_dict = {i: i * i for i in range(9)}
        test_set = {i for i in range(9)}
        print("dict & set", test_dict, test_set)

    @staticmethod
    def debugging_scripts():
        # import pdb
        # pdb.set_trace()
        pass

    @staticmethod
    def detect_python_version_at_runtime():
        import sys
        # if not hasattr(sys, "version_info") or sys.version_info >= (3, 5):
        if not hasattr(sys, "hexversion") or sys.hexversion != 50660080:
            print("Oh, you are not running on Python 3.5")
            # sys.exit(1)
        print("Current version is:", sys.version_info)

    @staticmethod
    def use_enums():
        class Shapes:
            Circle, Square, Triangle, Quadrangle = range(4)

        print("enums items:", Shapes.Circle, Shapes.Triangle)

    @staticmethod
    def dictionary_switch():
        std_calc = {
            "sum": lambda x, y: x + y,
            "sub": lambda x, y: x - y
        }
        print("Result of dictionary switch:", std_calc["sum"](std_calc["sub"](8, 3), 4))

    @staticmethod
    def about_method():
        test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
        print("With in max:", max(set(test), key=test.count))

    @staticmethod
    def reset_recursion_limit():
        import sys
        print("recursionlimit:", sys.getrecursionlimit())
        sys.setrecursionlimit(sys.getrecursionlimit() + 1)
        print("new recursionlimit:", sys.getrecursionlimit())

    @staticmethod
    def memory_object(x=1):
        import sys
        # python 2.7 -> 24
        # python 3.5 -> 28
        print("memory:", sys.getsizeof(x))

    @staticmethod
    def about_chain():
        import itertools
        test = [[2, 3], [4, 5], [9, 0]]
        print("chain list", list(itertools.chain.from_iterable(test)))

    @staticmethod
    def switch_from_dict():
        def x_switch(name):
            return x_switch._inside.get(name, None)

        x_switch._inside = {"a": 1, "b": 2, "c": 3}
        print("switch:", x_switch("a"), x_switch("c"))


if __name__ == '__main__':
    # print(vars(EssentialTipsAndTricks).items())
    for method in dir(EssentialTipsAndTricks):
        if not method.startswith("_"):
            fn = getattr(EssentialTipsAndTricks, method, None)
            if callable(fn):
                print("\n\t", fn.__name__)
                fn()
