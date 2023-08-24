#!/usr/bin/python3
"""Retrieves and prints a sorted list of states from a MySQL database."""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4: sys.exit("Usage: {} <username> <password> <database>".format(sys.argv[0]))
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    [print(row) for row in cursor.fetchall()]
    cursor.close()
    db.close()
