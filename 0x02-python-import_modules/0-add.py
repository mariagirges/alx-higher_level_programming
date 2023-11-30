#!/usr/bin/python3
a = 1
b = 2
from add_0 import add
add_0 = __import__('add_0')
result = add_0.add(a, b)
print('{} + {} = {}'.format(a, b, result))
