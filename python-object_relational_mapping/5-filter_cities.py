#!/usr/bin/python3
"""Lists all cities of a state from hbtn_0e_4_usa database"""
import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cur = conn.cursor()
    query = "SELECT cities.name FROM cities "
    query += "JOIN states ON cities.state_id = states.id "
    query += "WHERE states.name = %s "
    query += "ORDER BY cities.id ASC"
    cur.execute(query, (state_name,))
    query_rows = cur.fetchall()

    city_names = [row[0] for row in query_rows]
    print(", ".join(city_names))

    cur.close()
    conn.close()
