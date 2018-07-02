import requests
import csv
from bs4 import BeautifulSoup, Comment
from pydfs_lineup_optimizer import * # version >= 2.0.1

'''
Fanduel Scraper that scrapes rotogur for predicitions and optimizes lineups in place
'''
class RotoGuruScraper():
    def __init__(self, url):
        self.url = url
        self.players = []
        self.finished_games = []
       
    def get_soup(self):
        page = requests.get(self.url)
        self.soup = BeautifulSoup(page.text, "html.parser")

    def get_players(self):
        for row in str(self.soup).split('\n')[:-1]:
            rows = row.split(",")
            names = rows[0][1:-1].split()
            pos = rows[3]
            team = rows[2]
            sal = rows[1]
            rotoProj = rows[7]

            self.players.append(rotoPlayer(names[0] + " " + names[1], sal, team, pos, rotoProj))
        return self.players

class rotoPlayer():
    def __init__(self, name, sal, team, pos, proj):
        self.name = name
        self.sal = sal
        self.team = team
        self.pos = pos
        self.proj = proj
