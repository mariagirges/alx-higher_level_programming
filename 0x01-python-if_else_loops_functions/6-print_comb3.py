#!/usr/bin/python3
for x in range(1,10):
    for y in range(x+1,10):
        if x == 8:
            if y == 9:
                print (89)
        print("{:d}{:d}".format(x, y), end=", ")
