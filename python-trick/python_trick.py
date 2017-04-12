#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/4/12


class EssentialTipsAndTricks:
    """
    http://www.techbeamers.com/essential-python-tips-tricks-programmers/
    """

    @staticmethod
    def print_file_path_of_imported_variables():
        import sys
        print(sys)

    @staticmethod
    def dictionary_set_comprehensions():
        test_dict = {i: i * i for i in range(9)}
        test_set = {i for i in range(9)}
        print(test_dict, test_set)

    @staticmethod
    def debugging_scripts():
        import pdb
        pdb.set_trace()

    @staticmethod
    def detect_python_version_at_runtime():
        import sys
        # if not hasattr(sys, "version_info") or sys.version_info >= (3, 5):
        if not hasattr(sys, "hexversion") or sys.hexversion != 50660080:
            print("Oh, you are not running on Python 3.5\n")
            sys.exit(1)

    @staticmethod
    def use_enums():
        class Shapes:
            Circle, Square, Triangle, Quadrangle = range(4)

        print(Shapes.Circle, Shapes.Triangle)

    @staticmethod
    def dictionary_switch():
        std_calc = {
            "sum": lambda x, y: x + y,
            "sub": lambda x, y: x - y
        }
        print(std_calc["sum"](std_calc["sub"](8, 3), 4))

    @staticmethod
    def about_method():
        test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
        print(max(set(test), key=test.count))

    @staticmethod
    def reset_recursion_limit():
        import sys
        print(sys.getrecursionlimit())
        sys.setrecursionlimit(sys.getrecursionlimit() + 1)
        print(sys.getrecursionlimit())

    @staticmethod
    def memory_object(x=1):
        import sys
        # python 2.7 -> 24
        # python 3.5 -> 28
        print(sys.getsizeof(x))

if __name__ == '__main__':
    pass
