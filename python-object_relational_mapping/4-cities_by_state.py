#!/usr/bin/python3
"""Lists all cities with state names from hbtn_0e_4_usa database"""
import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cur = conn.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities "
    query += "JOIN states ON cities.state_id = states.id "
    query += "ORDER BY cities.id ASC"
    cur.execute(query)
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
