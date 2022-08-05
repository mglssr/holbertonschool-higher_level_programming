#!/usr/bin/python3
""" Write a script that lists all states from the database hbtn_0e_0_usa"""


if __name__ == "__main__":
    import MySQLdb
    import sys

    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=user,
                         passwd=passwd, db=db)
    cur = db.cursor()
    query = "SELECT cities.name FROM cities WHERE state_id\
            IN(SELECT id FROM states WHERE name = %s) ORDER BY ID ASC"
    cur.execute(query, (state,))
    rows = cur.fetchall()
    for row in rows[:-1]:
        print(f"{row[0]}, ", end="")
    if rows:
        print(rows[-1][0])
    else:
        print()
    cur.close()
    db.close()
