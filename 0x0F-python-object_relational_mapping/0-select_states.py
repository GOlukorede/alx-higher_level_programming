#!/usr/bin/python3
import MySQLdb
from sys import argv

"""
 script that lists all states from the database hbtn_0e_0_usa
"""

if __name__ == "__nain__":
    """
    To access the database and list ass states
    """
  
    mydb = MySQLdb.connect(host="localhost", username=argv[1], password=argv[2], db=argv[3] port=3306)

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM states")
    myresult = mycursor.fetchall()
    for states in myresult:
        print(states)
