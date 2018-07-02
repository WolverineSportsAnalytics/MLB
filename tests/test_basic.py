# this is the first of our testing files so that we can keep everything all Up and running
import unittest
import constants
import mysql.connector
import sys
from os import path
sys.path.append("Scrapers" )
sys.path.append("../Scrapers" )
import playerReferenceScraper


class TestDataBaseConnection(unittest.TestCase):
    def test_connect(self):
         try:
            cnx = mysql.connector.connect(user=constants.testUser,
                host=constants.testHost,
                database=constants.testName,
                password=constants.testPassword)                                                                                                               
            cusror = cnx.cursor()
            self.assertEqual(1, 1)
         except :
            self.assertEqual(0, 1)

if __name__ == '__main__':
    unittest.main()
