#!/usr/bin/python3
import MySQLdb
import sys

"""Connect to the MySQL server"""
conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3]
)

"""Create a cursor object"""
cur = conn.cursor()

"""Execute the SELECT statement"""
cur.execute("SELECT * FROM states ORDER BY states.id ASC")

"""Fetch and print the results"""
results = cur.fetchall()
for row in results:
    print(row)

"""Close the cursor and connection"""
cur.close()
conn.close()
