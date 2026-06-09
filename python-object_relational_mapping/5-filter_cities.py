#!/usr/bin/python3
"""
Lists all cities of a state given as argument from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    state_name = sys.argv[4]

    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()

    cities_list = [row[0] for row in rows]
    print(", ".join(cities_list))

    cursor.close()
    db.close()
