import unittest
import mysql.connector
import sys 
from os import path
from MLB_Engine import RotoWireScraper as rws
from bs4 import BeautifulSoup, Comment

class TestRotowirePlayers(unittest.TestCase):
    def test(self):
        roto = rws.RotoScraper("")
        with open("tests/rotoMock.txt") as src:
            page = src.read()
        roto.soup = BeautifulSoup(page, 'html.parser')

        players = roto.get_players()
        
        namedPlayers = []
        bryce = []
        for player in players:
            namedPlayers.append(player.name)
            if player.name == "Bryce Harper":
                bryce = player

        self.assertTrue("Daniel Murphy" in namedPlayers)
        self.assertTrue("Bryce Harper" in namedPlayers)
        self.assertEqual(bryce.sal, "4400")
