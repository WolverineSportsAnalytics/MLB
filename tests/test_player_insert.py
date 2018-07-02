import unittest
import mysql.connector
import sys 
from os import path
from MLB_Engine import RotoGuruScraperMLB as rgs
from MLB_Engine import RotoWireScraper as rws
from bs4 import BeautifulSoup, Comment
import datetime


class TestRotoGuruPlayers(unittest.TestCase):
    def test(self):
        roto = rgs.RotoGuruScraper("")
        with open("tests/rotoGuruMockPitchers.txt") as src:
            page = src.read()
        roto.soup = BeautifulSoup(page, 'html.parser')
        # this depends on other rotogure test working

        players = roto.get_players()

        cnx = mysql.connector.connect(user="root",
                host="127.0.0.1",
                database="mlb",
                password="")                                                                                                               
        cursor = cnx.cursor()
        
        today = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        for player in players:
            player.insertTable(cursor, today)

        cnx.commit()

        cursor.execute("Select Salary from players where Name=\"Madison Bumgarner\"")
        sal = cursor.fetchall()[0][0]
        self.assertEqual(sal, 8100)

class TestRotoGrinderPlayers(unittest.TestCase):
     def test(self):
        roto = rgs.RotoGuruScraper("")
        with open("tests/rotoGuruMockPitchers.txt") as src:
            page = src.read()
        roto.soup = BeautifulSoup(page, 'html.parser')
        # this depends on other rotogure test working

        players = roto.get_players()

        cnx = mysql.connector.connect(user="root",
                host="127.0.0.1",
                database="mlb",
                password="")                                                                                                               
        cursor = cnx.cursor()
        
        today = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        for player in players:
            player.insertTable(cursor, today)

        roto = rws.RotoScraper("")
        with open("tests/rotoMock.txt") as src:
            page = src.read()
        roto.soup = BeautifulSoup(page, 'html.parser')

        players = roto.get_players()
        
        for player in players:
            player.insertTable(cursor, today)
        
        cnx.commit()
        
        cursor.execute("select RotoGrindersProjection, RotoWireProjection from players where Name=\"Madison Bumgarner\";")

        grinder, wire = cursor.fetchall()[0]
        self.assertEqual(grinder,28.26 )
        self.assertEqual(wire, 39.66)

class TestMultipledays(unittest.TestCase):
    def test(self):
        #TODO impliment me
        self.assertEqual(0, 0)
