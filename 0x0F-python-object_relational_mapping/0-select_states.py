#!/usr/bin/python3
""" retrieves and lists all states from the hbtn_0e_0_usa database. """
import MySQLdb
import sys


if __name__ == "__main__":
    sql = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    sql_cursor = sql.cursor()
    sql_cursor.execute("SELECT * FROM states")
    rows = sql_cursor.fetchall()
    for row in rows:
        print(row)
    sql_cursor.close()
    sql.close()
