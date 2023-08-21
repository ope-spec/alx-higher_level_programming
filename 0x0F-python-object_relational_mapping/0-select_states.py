#!/usr/bin/python3

""" This script retrieves and displays all states from the hbtn_0e_0_usa database."""
import MySQLdb
import sys


def retrieve_and_display_states():
    if len(sys.argv) != 4:
        print("Usage: python3 script_name.py <username> <password> <database>")
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        db = MySQLdb.connect(host="localhost", user=username,
                             passwd=password, db=database, port=3306)
        cur = db.cursor()
        cur.execute("SELECT * FROM states")
        rows = cur.fetchall()

        for row in rows:
            print(row)

        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    retrieve_and_display_states()
