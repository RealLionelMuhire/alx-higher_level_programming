#!/usr/bin/python3
m = 1
for p in range(90, 64, -1):
    if m % 2 == 0:
        alpha = chr(p + 32)
        print("{}".format(alpha), end='')
    else:
        alpha = chr(p)
        print("{}".format(alpha), end='')
    m += 1
