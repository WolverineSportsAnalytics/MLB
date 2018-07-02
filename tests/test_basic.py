# this is the first of our testing files so that we can keep everything all Up and running
import unittest
import mysql.connector
import sys
from os import path


class TestDataBaseConnection(unittest.TestCase):
    def test_connect(self):
         try:
            cnx = mysql.connector.connect(user="root",
                host="127.0.0.1",
                database="mlb",
                password="")                                                                                                               
            cusror = cnx.cursor()
            self.assertEqual(1, 1)
         except Exception as e:
             print e
             self.assertEqual(0, 1)

if __name__ == '__main__':
    unittest.main()
