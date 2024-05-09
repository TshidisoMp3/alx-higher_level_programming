#!/usr/bin/python3

""" Filter states by user input"""

import sys
import MySQLdb

# Connect to a MySQL database

if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]
    )
    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in c.fetchall() if state[1][0] == "n"]
    c.close()
    db.close()
