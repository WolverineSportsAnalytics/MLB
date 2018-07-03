import RotoGuruScraperMLB as rgs
import RotoWireScraper as rws
import MlbOptimizer 
import mysql.connector
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup, Comment
import time



class Slate():
    def __init__(self, teams, name):
        self.teams = teams
        self.name = name


class WsaEngine():
    def __init__(self):
        self.rgsHitters = rgs.RotoGuruScraper("https://rotogrinders.com/projected-stats/mlb-hitter.csv?site=fanduel")
        self.rgsPitchers = rgs.RotoGuruScraper("https://rotogrinders.com/projected-stats/mlb-pitcher.csv?site=fanduel")
        self.rws = rws.RotoScraper( "https://www.rotowire.com/daily/mlb/optimizer.php?site=FanDuel&sport=mlb")
        
    def get_slates(self):
        chrome_options = Options()  
        chrome_options.add_argument("--headless")  
        browser = webdriver.Chrome(executable_path=("./chromedriver"),   chrome_options=chrome_options)
        
        url = "https://rotogrinders.com/lineuphq/mlb?site=fanduel"
        browser.get(url) #navigate to the page
        browser.find_element_by_id("slate-menu-link").click()
        time.sleep(3)
        page =browser.find_element_by_id("slate-select-menu").get_attribute("innerHTML")
        soup = BeautifulSoup(page, "html.parser")
        slates = soup.find_all("li",{"class": "slate-menu__slate"})
        
        slate_list = []
        for slate in slates:
            name = slate.find_all("b",{"class": "slate-menu__label"})[0].find("span").text
            games = slate.find_all("li",{"class": "slate-menu__game"})
            teams = []
            for game in games:
                split = game.find("span").text.split()
                teams.append(split[0])
                teams.append(split[2])
            slate_list.append(Slate(teams, name))
        
        browser.quit()
        self.slates = slate_list

    def setLineups(self, cursor, cnx, date):
        scrapers = [self.rws, self.rgsHitters, self.rgsPitchers]
        for scraper in scrapers:
            scraper.get_soup() # go get the text 
            for player in scraper.get_players(): # parse out the players
                player.insertTable(cursor, date) # insert all the players

        
        cursor.execute("Delete from players where RotoWireProjection is null")
        
        cnx.commit()
         
        gameTimes, startTimes = self.rws.get_game_times()

        opt = MlbOptimizer.MlbOptimizer(date, cursor)
        opt.getPlayers(date)
        for time in startTimes:
            opt.generateLineups("rotowire", 1, date, time, gameTimes)
            opt.insertLineups(cursor)
            opt.generateLineups("rotoGrinders", 1, date, time, gameTimes)
            opt.insertLineups(cursor)
            opt.generateLineups("average", 1, date, time, gameTimes)
            opt.insertLineups(cursor)

    # gets lineups for that are closest to a specific time
    def getLineups(self, cursor, date, time):

       
        self.rws.get_soup() 
        gameTimes, startTimes = self.rws.get_game_times()
        startTimes = sorted(startTimes)
        closestStart = 0
        
        for sTime in startTimes:
            if closestStart <= sTime:
                closestStart = sTime


        query = "Select * from lineups where date=%s and lineupTime=%s"
        cursor.execute(query, (date, closestStart))
        return cursor.fetchall()

    # get all lineups for a day
    def getAllLineups(self, cursor, date):

        query = "Select * from lineups where date=%s"
        cursor.execute(query, (date,) )
        return cursor.fetchall()
        

def genMlbLineups():
        cnx = mysql.connector.connect(user="root",
                host="127.0.0.1",
                database="mlb",
                password="")                                                                                                               
        cursor = cnx.cursor()
        
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        time = datetime.datetime.now().strftime('%H:%M:%S')

        gen = WsaEngine()
        gen.get_slates()
        gen.setLineups(cursor,cnx, today)

        cnx.commit()

if __name__=="__main__":
    genMlbLineups()
