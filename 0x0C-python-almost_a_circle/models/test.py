#!/usr/bin/python3
class Myclass:
    def __init__(self):
        pass

    def retName(self):
        return self.__class__.__name__

my_ob = Myclass()
print(my_ob.retName() + ".json")
