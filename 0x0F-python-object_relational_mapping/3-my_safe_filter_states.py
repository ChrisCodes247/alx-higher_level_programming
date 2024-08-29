#!/usr/bin/python3

"""
    A script that lists all states that starts with a name
    The name is inputted as an argument
"""

import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], host='localhost', port=3306)

    cursor = db.cursor()

    search_name = sys.argv[4]

    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
    
    cursor.execute(query, (search_name,))

    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()
