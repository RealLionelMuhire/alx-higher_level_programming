#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ln = len(argv)
    sum = 0
    int(sum)
    if ln < 2:
        print("{}".format(sum))
    else:
        n = 1
        while n < ln:
            sum += int(argv[n])
            n += 1
        print("{}".format(sum))
