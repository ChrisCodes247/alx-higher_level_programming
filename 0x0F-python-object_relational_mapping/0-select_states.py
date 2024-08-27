#!/usr/bin/python3

import MySQLdb

db = MySQLdb.connect(host="localhost", port=3306, user="test", password="password", database="hbtn_0e_0_usa")

c = db.cursor()
c.execute("""SELECT * FROM states ORDER BY states.id ASC""")
c.fetchall()
