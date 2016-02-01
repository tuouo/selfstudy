#!/usr/bin/env python3
# -*- coding: utf-8 -*-

exec("print('Hello World.')")
exec("""for i in range(5):
	print("iter time: {}".format(i))
	""")

print(int(7.6))
exec("int = 3")
print(type(int), int) # int 3

g = {'a':7, 'b':8}
exec("global a; print(a, b)", g)

g = {'a':7, 'b':8}
l = {'b':9, 'c':10}
exec("global a; print(a, b, c)", g, l)


import math
def compile_(s):
    code = """def f(x):\n    return {}""".format(s) # Wrap the string as a function f(x).
    scope = {"sin": math.sin, "cos": math.cos}      # Define the scope for the code to use.
    exec(code, scope)                               # Execute code inside the given scope
    return scope["f"]                               # Extract it

fn = compile_("x*2 + 2 * sin(x)")
print(fn(math.pi / 2))