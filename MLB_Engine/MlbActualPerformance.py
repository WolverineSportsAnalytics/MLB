import mysql.connector
import datetime
from selenium import webdriver
import WsaLineups
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.common.keys import Keys
from django.core.cache import cache
from bs4 import BeautifulSoup, Comment
import time, os

cnx = mysql.connector.connect(user="wsa@wsabasketball",
                host="wsabasketball.mysql.database.azure.com",
                database="mlb",
                password="LeBron>MJ!")
cursor = cnx.cursor()

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(executable_path=("./chromedriver"),   chrome_options=chrome_options)
url = "https://www.linestarapp.com/Projections/Sport/MLB/Site/FanDuel/PID/1044"
browser.get(url) #navigate to the page 

finals = browser.find_elements_by_class_name("salarybox")

pairs = []
for fin in finals:
	pairs.append((fin.find_elements_by_class_name("salaryboxLive")[0].text, fin.find_elements_by_class_name("playername")[0].text))
browser.close()

stmt = "Update players set fanduelPoints=%s where name=%s and date=\"2018-07-05\";"
for pair in pairs:
	inserts = (float(pair[0].split()[1]), " ".join(pair[1].split()[-2:]))
        
	try:
		cursor.execute(stmt, inserts)
	except Exception as e:
                print e
		print pair[1].split()[-2:]
	
cnx.commit()
cursor.close()
cnx.close()
