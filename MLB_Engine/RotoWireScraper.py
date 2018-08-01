import requests
from bs4 import BeautifulSoup, Comment
from pydfs_lineup_optimizer import * # version >= 2.0.1
import datetime
from pytz import timezone
from WsaPlayer import WsaPlayer
import json

'''
Fanduel Scraper that scrapes rotoWire for predicitions and returns a WsaPlayer list
'''

class RotoScraper():
    def __init__(self, url):
        self.url = url
        self.players = []
        self.gameTimes = {}
        self.startTimes = []

    # Returns Dictionary of key:team value:starttime as well as a set of all start times
    def get_game_times(self):
        games = self.soup.find("div",{"id":"rwo-matchups"}).find_all("div",{"class":"rwo-game-team"})
        zone = timezone("US/Eastern")
        now = datetime.datetime.now(tz=zone).time().strftime('%H:%M:%S')
        for game in games:
            team = game['data-team']
            time = game['data-gametimeonly']
            self.gameTimes[team] = time
            self.startTimes.append(time)

        return self.gameTimes, set(self.startTimes)
    
    def get_soup(self):
	pass # no longer need Beutiful soup as page is in JSON

    def get_players(self):
        page = requests.get(self.url)
	players = json.loads(str(page.text)) # Load from JSON

        for player in players:
            try:
                first_name = player['first_name'] 
                last_name = player['last_name']
                name = first_name + ' ' + last_name
                
                
                team  = player['team'] 

                pos = player['position'] # pos
                if pos == 'C1':
                    pos = ['1B','C']
                else:
                    pos = [str(pos)]

                sal = player['salary']
                rotoProj = player['proj_rotowire']
                self.players.append(WsaPlayer(name, sal, team, pos, rotoProj, None))

            except Exception as e:
                print e

        return self.players
