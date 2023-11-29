#!/usr/bin/python3
for x in range(ord('z'), ord('a') - 1, -1):
    case = "lower" if x % 2 == 0 else "upper"
    print("{}".format(chr(x).lower() if case == "lower" else chr(x)), end=" ")
