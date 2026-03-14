#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Accessing command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connecting to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Creating a cursor object to execute queries
    cursor = db.cursor()

    # Executing the SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetching all the rows
    rows = cursor.fetchall()

    # Displaying the results
    for row in rows:
        print(row)

    # Closing the cursor and the database connection
    cursor.close()
    db.close()
