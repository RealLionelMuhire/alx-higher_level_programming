#!/usr/bin/python3
import unittest
import json
import os
from serialized_class import Myclass

class TestMyclass(unittest.TestCase):

    def setUp(self):
        self.test_obj = Myclass("Lionel", "218008609", "CMHS")
        self.test_file = "UniTest.json"

    def tearDown(self):
        """To clean up file used in testing"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_to_json_file(self):
        #Testing serialization and file availability
        self.test_obj.to_json_file(self.test_file)
        self.assertTrue(os.path.exists(self.test_file))

    def test_from_json(self):
        #Testing deserialization from file
        with open(self.test_file, 'w') as file:
            json.dump(self.test_obj.__dict__, file)

        obj_dict = Myclass.from_json_file(self.test_file)
        self.assertEqual(obj_dict, self.test_obj.__dict__)

    def test_username(self):
        #test getter and setter for username
        self.assertEqual(self.test_obj.username, "Lionel")

        new_username = "Leo"
        self.test_obj.username = new_username
        self.assertEqual(self.test_obj.username, new_username)



    def test_school(self):
        #test getter and setter for school
        self.assertEqual(self.test_obj.school, "ALX")
        
        new_school = "ALX_SE"
        self.test_obj.school = new_school
        self.assertEqual(self.test_obj.school, new_school)

    def test_user_id(self):
        #test getter and setter for user_id
        self.assertEqual(self.test_obj.user_id, "19737")

        new_user_id = "00001"
        self.test_obj.user_id = new_user_id
        self.assertEqual(self.test_obj.user_id, new_user_id)


if __name__ == "__main__":
    unittest.main()
