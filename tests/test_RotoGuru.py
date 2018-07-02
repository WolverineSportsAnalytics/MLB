import unittest
import mysql.connector
import sys 
from os import path
from MLB_Engine import RotoGuruScraperMLB as rgs
from bs4 import BeautifulSoup, Comment

class TestRotoGuruPlayers(unittest.TestCase):
    def test(self):
        roto = rgs.RotoGuruScraper("")
        with open("tests/rotoGuruMockPitchers.txt") as src:
            page = src.read()
        roto.soup = BeautifulSoup(page, 'html.parser')

        players = roto.get_players()
        
        namedPlayers = []
        alex = []
        for player in players:
            namedPlayers.append(player.name)
            if player.name == "Alex Wood":
                alex = player

        self.assertTrue("Corey Kluber" in namedPlayers)
        self.assertTrue("Alex Wood" in namedPlayers)
        self.assertEqual(alex.sal, "8300")


        with open("tests/RotoGrindersHittersMock.txt") as src:
            page = src.read()
        roto.soup = BeautifulSoup(page, 'html.parser')

        players = roto.get_players()
        
        namedPlayers = []
        bryce = []
        for player in players:
            namedPlayers.append(player.name)
            if player.name == "Bryce Harper":
                bryce = player

        self.assertTrue("Bryce Harper"== bryce.name)
        self.assertEqual(bryce.sal, "4400")


class TestRotoGuruSoup(unittest.TestCase):
    def test(self):
        url = "https://www.rotowire.com/daily/mlb/optimizer.php?site=FanDuel&sport=mlb"
        roto = rgs.RotoGuruScraper(url)
        roto.get_soup()

        self.assertTrue(roto.soup is not None)

