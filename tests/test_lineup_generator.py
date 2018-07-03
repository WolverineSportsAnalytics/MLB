import unittest
import mysql.connector
import sys 
from os import path
sys.path.append("../../MLB")
from MLB_Engine import RotoGuruScraperMLB as rgs
from MLB_Engine import WsaLineups, MlbOptimizer
from MLB_Engine import RotoWireScraper as rws
from bs4 import BeautifulSoup, Comment
import datetime

class TestGameTime(unittest.TestCase):
    def test(self):
        roto = rws.RotoScraper("")
        with open("tests/rotoMock.txt") as src:
            page = src.read()
        roto.soup = BeautifulSoup(page, 'html.parser')

        gameTimes, startTimes = roto.get_game_times()

        self.assertEqual(gameTimes["DET"], "13:07:00")

class TestStartTime(unittest.TestCase):
    def test(self):
        roto = rws.RotoScraper("")
        with open("tests/rotoMock.txt") as src:
            page = src.read()
        roto.soup = BeautifulSoup(page, 'html.parser')

        gameTimes, startTimes = roto.get_game_times()

        self.assertTrue("13:07:00" in startTimes)

class TestLineupObject(unittest.TestCase):
    def test(self):

        cnx = mysql.connector.connect(user="root",
                host="127.0.0.1",
                database="mlb",
                password="")                                                                                                               
        cursor = cnx.cursor()
        
        players = ["Chris Sale", "Greg Bird", "Yoan Moncada", "David Freese", "Elvis Andrus", "Tommy Pham", "Avisail Garcia", "Charlie Blackmon", "Salvador Perez"]
        points = 137.17
        today = "2018-07-02"
        wsa = WsaLineups.WsaLineup(players, today, "13:07:00", points, "rotowire")
        wsa.insertTable(cursor, 1)
        cnx.commit()

class TestLineupGenerator(unittest.TestCase):
    def test(self):

        cnx = mysql.connector.connect(user="root",
                host="127.0.0.1",
                database="mlb",
                password="")                                                                                                               
        cursor = cnx.cursor()
        today = "2018-07-02"

        optimize = MlbOptimizer.MlbOptimizer(today, cursor)
        
        roto = rws.RotoScraper("")
        with open("tests/rotoMock.txt") as src:
            page = src.read()
        roto.soup = BeautifulSoup(page, 'html.parser')

        gameTimes, startTimes = roto.get_game_times()
        print gameTimes

        optimize.generateLineups("rotowire", 2, today, "00:00:01", gameTimes)
        self.assertEqual(optimize.my_lineups[1].points, 138.37)

    def testInsert(self):
        cnx = mysql.connector.connect(user="root",
                host="127.0.0.1",
                database="mlb",
                password="")                                                                                                               
        cursor = cnx.cursor()
        today = "2018-07-02"
        optimize = MlbOptimizer.MlbOptimizer(today, cursor)
        
        roto = rws.RotoScraper("")
        with open("tests/rotoMock.txt") as src:
            page = src.read()
        roto.soup = BeautifulSoup(page, 'html.parser')

        gameTimes, startTimes = roto.get_game_times()

        optimize.generateLineups("rotowire", 2, today, "00:00:01", gameTimes)
        optimize.insertLineups(cursor)
        cnx.commit()

        

if __name__ =="__main__":
    unittest.main()
