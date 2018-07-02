import unittest
import mysql.connector
import sys 
from os import path
from MLB_Engine import RotoGuruScraperMLB as rgs
from MLB_Engine import WsaLineups
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

class TestGameTime(unittest.TestCase):
    def test(self):
        roto = rws.RotoScraper("")
        with open("tests/rotoMock.txt") as src:
            page = src.read()
        roto.soup = BeautifulSoup(page, 'html.parser')

        gameTimes, startTimes = roto.get_game_times()

        self.assertTrue("13:07:00" in startTimes)

class TestLineupGenerator(unittest.TestCase):
    def test(self):

        cnx = mysql.connector.connect(user="root",
                host="127.0.0.1",
                database="mlb",
                password="")                                                                                                               
        cursor = cnx.cursor()
        
        today = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        players = ["Chris Sale", "Greg Bird", "Yoan Moncada", "David Freese", "Elvis Andrus", "Tommy Pham", "Avisail Garcia", "Charlie Blackmon", "Salvador Perez"]
        points = 137.17
        today = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        wsa = WsaLineups.WsaLineup(players, today, "13:07:00", points)
        wsa.insertTable(cursor, 1)
        cnx.commit()
        
