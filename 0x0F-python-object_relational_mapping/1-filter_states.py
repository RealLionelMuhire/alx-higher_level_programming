#!/usr/bin/python3

"""this selects all enties which starts with N"""


def main():
    """this fx selects all those starts with N"""

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)

    cur = db.cursor()

    cur.execute(
        "SELECT id, name FROM states WHERE ASCII(name) LIKE ASCII('N');"
    )
    [print(item) for item in cur.fetchall()]

    cur.close()
    db.close()


if __name__ == '__main__':
    main()
