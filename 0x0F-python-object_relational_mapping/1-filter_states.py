#!/usr/bin/python3
""" Write a script that lists all states from the database hbtn_0e_0_usa"""


if __name__ == "__main__":
    import MySQLdb
    import sys


    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=user,
                         passwd=passwd, db=db)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name REGEXP '^[N]'")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
