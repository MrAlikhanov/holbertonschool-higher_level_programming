#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Ensures that all rows (e.g., up to 10 or more) are retrieved.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if arguments are provided (Username, Password, DB Name)
    if len(sys.argv) < 4:
        exit(1)

    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db_name
    )

    cursor = db.cursor()

    # The SQL query: 
    # 1. No "LIMIT" clause so we get every row.
    # 2. Ordered by ID so 1-10 appear in sequence.
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetching all results
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # Close connections
    cursor.close()
    db.close()
