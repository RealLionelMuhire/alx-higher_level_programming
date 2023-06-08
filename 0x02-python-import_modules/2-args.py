#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ln = len(argv)
    if ln == 1:
        print("{} arguments.".format(ln - 1))
    if ln == 2:
        print("{} argument:".format(ln - 1))
        print("{}: {}".format(1, argv[1]))
    elif ln > 2:
        print("{} arguments:".format(ln - 1))
        n = 1
        while n < ln:
            print("{}: {}".format(n, argv[n]))
            n += 1
