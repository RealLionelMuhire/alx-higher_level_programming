#!/usr/bin/python3

import json

class Myclass:
    def __init__(self, username, user_id, school):
        self._username = username
        self._user_id = user_id
        self._school = school

    def to_json_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)

    @staticmethod
    def from_json_file(filename):
        with open(filename, 'r') as file:
            j_data = file.read()
            obj_dict = json.loads(j_data)
        return obj_dict

    @property
    def school(self):
        return self._school

    @school.setter
    def school(self, value):
        self._school = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


my_obj = Myclass("Lionel", "218008609", "CHMS")


my_obj_str = my_obj.to_json_file("My_Obj.json")

from_json_obj = Myclass.from_json_file("My_Obj.json")
print(from_json_obj)
