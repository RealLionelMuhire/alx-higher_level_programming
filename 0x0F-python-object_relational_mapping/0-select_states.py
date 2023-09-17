#!/usr/bin/python3

"""
this script will take 3 arguments, mysql usename, pws, database name
"""

import MySQLdb
from sys import argv


def main():
    """this function is to execute db select*"""
    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states;")
    [print(item) for item in cur.fetchall()]

    cur.close()
    db.close()


if __name__ == '__main__':
    main()
