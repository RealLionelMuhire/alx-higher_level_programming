#!/usr/bin/python3
"""Add all  arguments to a list and save them to a file"""
import sys
if __name__ == "__main__":
    save_to_json = __import__('5-save_to_json_file').save_to_json_file

    load_from_json = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]
try:
    exist_data = load_from_json('add_item.json')
except FileNotFoundError:
    exist_data = []
exist_data.extend(args)
save_to_json(exist_data, 'add_item.json')
