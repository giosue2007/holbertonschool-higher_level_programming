#!/usr/bin/python3
"""Lists all states matching the argument from the database."""
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=MY_USER,
        passwd=MY_PASS,
        db=MY_DB,
    )
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(MY_DB)
        
    
    )
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
