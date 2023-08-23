#!/usr/bin/python3
""" retrieves and lists all states from the hbtn_0e_0_usa database. """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    sql = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    sql_cursor = sql.cursor()
    sql_cursor.execute("SELECT * FROM states ORDER BY id ASC")
    state_records = sql_cursor.fetchall()
    for state in state_records:
        print(state)
    sql_cursor.close()
    sql.close()
