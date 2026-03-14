#!/usr/bin/python3
"""
Verilənlər bazasından ID-si 4 və daha böyük olan ştatları siyahılayır.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Arqumentləri əldə edirik
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # MySQL serverinə qoşuluruq
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db_name
    )

    cursor = db.cursor()

    # SQL sorğusuna WHERE şərti əlavə edirik (məsələn, ID >= 4)
    # Əgər konkret olaraq hansısa başqa şərt lazımdırsa, buranı dəyişə bilərsiniz.
    query = "SELECT * FROM states WHERE id >= 4 ORDER BY id ASC"
    
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
