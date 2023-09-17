#!/usr/bin/pyton3

"""inserting cities"""


def main():
    import MyMSQLdb
    import sys import argv

    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                         db=argv[3],port=3306)
    
    cur = db.cursor()
    cur.execute(
        ""
    )
    cur.close()
    db.close()


if __name__ = '__main__':
    main()
