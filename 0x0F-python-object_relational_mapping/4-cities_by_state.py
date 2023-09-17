#!/usr/bin/python3

"""inserting cities"""


def main():
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    
    cur = db.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN\
        states ON cities.id = states.id ORDER BY cities.id ASC;"
    )
    cur.close()
    db.close()


if __name__ == '__main__':
    main()
