#!/usr/bin/python3

"""this is for searching once it finds the name and list"""


def main():
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)

    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY %s;", (str(argv[4]),)
    )
    [print(item) for item in cur.fetchall()]

    cur.close()
    db.close()


if __name__ == '__main__':
    main()
