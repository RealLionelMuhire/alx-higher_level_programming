#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_len = len(sys.argv)
    if arg_len == 1:
        print("{} arguments.".format(arg_len - 1))
    if arg_len == 2:
        print("{} argument.".format(arg_len - 1))
        print("{}: {}".format(1, sys.argv[1]))
    elif arg_len > 2:
        print("{} arguments:".format(arg_len - 1))
        n = 0
        for arg in range(arg_len):
            n += 1
            if n > arg_len - 1:
                break
            print("{}: {}".format(n, sys.argv[n]))
