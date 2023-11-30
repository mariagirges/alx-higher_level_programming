#!/usr/bin/python3


import sys


def add(*args):
    total = sum(int(arg) for arg in args)
    print(total)


if __name__ == "__main__":
    arguments = sys.argv[1:]
    add(*arguments)
