#!/usr/bin/python3

"""
    A script that lists all cities from the database hbtn_0e_0_usa
    Username, password and database names are given as user args
"""

import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], host='localhost', port=3306)

    cursor = db.cursor()
    
    cursor.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = '{}' ORDER BY cities.id ASC".format(sys.argv[4]))

    data = cursor.fetchall()
    
    print(data)

    cursor.close()
    db.close()
