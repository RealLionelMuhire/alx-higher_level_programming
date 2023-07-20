#!/usr/bin/python3
from models.base import Base
import unittest
import os
import json
"""testing class for base"""


class Test_base(unittest.TestCase):
    """test base class for rectangles"""
    def test_to_json_str_emty(self):
        """test empty list"""
        list_d = []
        my_str = Base.to_json_string(list_d)
        self.assertTrue(my_str, "[]")

    def test_to_j_none(self):
        """test None list"""
        list_d = None
        my_str = Base.to_json_string(list_d)
        self.assertTrue(my_str, "[]")

    def test_to_js_list(self):
        """testing non-empty list"""
        list_d = [{"id": "66", "name": "Muhire"}, {"id": "99", "name": "Lio"}]
        my_js_str = Base.to_json_string(list_d)
        self.assertTrue(my_js_str, str(list_d))

    def test_saved_file(self):
        """testing the the json file is being saved"""
        class TestClass(Base):
            def __init__(self, id):
                super().__init__(id)

            def to_dictionary(self):
                return {"id": self.id}

        obj1 = TestClass(1)
        obj2 = TestClass(2)
        list_objs = [obj1, obj2]

        Base.save_to_file(list_objs)
        with open("Base.json", 'r') as file:
            data = json.load(file)
        expected_data = [{"id": 1}, {"id": 2}]
        self.assertEqual(data, expected_data)


if __name__ == "__main__":
    unittest.main()
