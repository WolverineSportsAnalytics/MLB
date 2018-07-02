import requests
from bs4 import BeautifulSoup, Comment
from pydfs_lineup_optimizer import * # version >= 2.0.1
import datetime
from pytz import timezone

'''
Fanduel Scraper that scrapes rotogur for predicitions and optimizes lineups in place
'''

class RotoScraper():
    def __init__(self, url):
        self.url = url
        self.players = []
        self.finished_games = []
       
    def get_soup(self):
        page = requests.get(self.url)
        self.soup = BeautifulSoup(page.text, "html.parser")

    def get_players(self):
        playersSoup = self.soup.find_all('tr')
        for i,count in zip(playersSoup[4:],range(len(playersSoup)-4)):
            try:
                name  = i.find_all('td')[1].text # name 
                names = name.split()
                name = names[0] + ' ' + names[1]
                
                
                team  = i.find_all('td')[2].text.rstrip()# team
                if team in self.finished_games:
                    continue

                pos = i.find_all('td')[3].text # pos
                if pos == 'C1':
                    pos = ['1B','C']
                else:
                    pos = [str(pos)]
                sal = i.find_all('td')[6].find('input')['value']
                sal = sal[1:]
                sals = sal.split(",")
                sal = sals[0] + sals[1]
                rotoProj = i.find_all('td')[7].find('input')['value']
                self.players.append(rotowirePlayer(name, sal, team, pos, rotoProj))

            except Exception as e:
                print e

        return self.players

class rotowirePlayer():
    def __init__(self, name, sal, team, pos, proj):
        self.name = name
        self.sal = sal
        self.team = team
        self.pos = pos
        self.proj = proj


def predict():
    url = "https://www.rotowire.com/daily/mlb/optimizer.php?site=FanDuel&sport=mlb"

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    games = soup.find("div",{"id":"rwo-matchups"}).find_all("div",{"class":"rwo-game-team"})
    zone = timezone("US/Eastern")
    now = datetime.datetime.now(tz=zone).time().strftime('%H:%M:%S')
    finished_games = []
    for game in games:
        team = game['data-team']
        time = game['data-gametimeonly']

        if now > time:
            finished_games.append(team)

if __name__ == "__main__":

    predict()
