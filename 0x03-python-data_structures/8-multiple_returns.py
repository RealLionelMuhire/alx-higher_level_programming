#!/usr/bin/python
def multiple_returns(sentence):
    if sentence == "":
        return 0, "None"
    else:
        n = 0
        my_list = list(sentence)
        while n < len(my_list):
            n += 1
        return n, my_list[0]
