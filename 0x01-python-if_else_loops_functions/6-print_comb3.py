#!/usr/bin/python3
for x in range(1,10):
    for y in range(x+1,10):
        print("{:d}{:d}".format(x, y), end=", " if y < 9 else "\n")
