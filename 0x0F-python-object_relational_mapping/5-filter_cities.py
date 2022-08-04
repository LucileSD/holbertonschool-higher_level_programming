#!/usr/bin/python3
"""
    lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states\
                ON states.id = cities.state_id\
                WHERE states.name=%s", (sys.argv[4],))
    rows = cur.fetchall()
    list = []
    for line in rows:
        for res in line:
            list.append(res)
    print(", ".join(list))
    cur.close()
    db.close()
