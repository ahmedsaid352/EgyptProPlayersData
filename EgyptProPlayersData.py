import csv
from selenium import webdriver
from selenium.webdriver.common import keys 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from time import sleep



name =[]
points=[]
goals =[]
assists=[]

print("please Enter integer number 1982-2021\n\n")

startingYear =int(input("starting year?\n\n").strip())

# startingYear = 2012
availableYears = 2022 - startingYear
availableYears = str(availableYears)
print("Note ! "+ availableYears +" years is available only \n\n" )
nOfYears = int(input("number of years \n\n").strip())
sleep(1)
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.maximize_window()

for i in range(nOfYears):

    browser.get(f"https://www.transfermarkt.com/scorer/topscorer/statistik/2021/plus/0/galerie/0?saison_id={startingYear+i}&art=profi&land_id=2&altersklasse=&ausrichtung=&spielerposition_id=&filter=0&yt0=Show")

    names = browser.find_elements_by_xpath('//*[@id="yw1"]/table/tbody/tr[*]/td[2]/table/tbody/tr[1]/td[2]/a')
    pts =   browser.find_elements_by_xpath('//*[@id="yw1"]/table/tbody/tr[*]/td[9]')
    goal=   browser.find_elements_by_xpath('//*[@id="yw1"]/table/tbody/tr[*]/td[7]')
    assist= browser.find_elements_by_xpath('//*[@id="yw1"]/table/tbody/tr[*]/td[8]')
    for i in range(len(names)):
        name.append(names[i].text)
        points.append(pts[i].text)
        goals.append(goal[i].text)
        assists.append(assist[i].text)

browser.quit()

information = {
    'Player Name':name,
    'goals':goals,
    'assist':assists,
    'Total goals & assists':points,
}


df = pd.DataFrame(information)

df.to_csv('EgyptProPlayers.csv',index=False)

print("Done! \n Data collected (needs cleaning) in EgyptProPlayers.csv")