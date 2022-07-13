import csv
from bs4 import BeautifulSoup
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
#yw1 > table > tbody > tr:nth-child(1) > td:nth-child(2) > table > tbody > tr:nth-child(1) > td.hauptlink > a
#yw1 > table > tbody > tr:nth-child(2) > td:nth-child(2) > table > tbody > tr:nth-child(1) > td.hauptlink > a

# define variables
name =[]
points=[]
goals =[]
assists=[]
nOfYears = 0
op = 0
art=""
startingYear=""
# user input
def user_input():
    print("please Enter integer number 1982-2021\n\n")
    global startingYear
    startingYear =int(input("starting year?\n\n").strip())
    availableYears = 2022 - startingYear
    availableYears = str(availableYears)
    print("Note ! "+ availableYears +" years is available only \n\n" )
    global nOfYears
    nOfYears = int(input("number of years \n\n").strip())
    sleep(1)
    print("\t\t menu options\n\n")
    print("1.all leagues & all cups\n\n")
    print("2.top leagues\n\n")
    print("3.top 10 leagues\n\n")
    op = int(input("Enter option number then press enter\n\n").strip())
    global art
    if (op==1):
        art= "profi"
    elif(op==2):
        art = "top"
    elif(op==3):
        art ="top10"
    else:
        print("Error you have to inter integer number 1:3\n\n please inter data again \n\n ")
        user_input()
    collectAndWriteData()
# collect data
def collectAndWriteData():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.maximize_window()
    for i in range(nOfYears):
        browser.get(f"https://www.transfermarkt.com/scorer/topscorer/statistik/2021/plus/0/galerie/0?saison_id={startingYear+i}&art={art}&land_id=2&altersklasse=&ausrichtung=&spielerposition_id=&filter=0&yt0=Show")
        html = browser.page_source
        soup = BeautifulSoup(html,"html.parser")

        names = soup.select('#yw1 > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(1) > td.hauptlink > a')
        pts   = soup.select('#yw1 > table > tbody > tr > td.zentriert.hauptlink')
        goal  = soup.select('#yw1 > table > tbody > tr > td:nth-child(7)')
        assist= soup.select('#yw1 > table > tbody > tr > td:nth-child(8)')
        for i in range(len(names)):
            name.append(names[i].text)
            points.append(int(pts[i].text))
            goals.append(int(goal[i].text))
            assists.append(int(assist[i].text))
    browser.quit()
    information = {
        'Player Name':name,
        'goals':goals,
        'assist':assists,
        'Total goals & assists':points,
    }
    df = pd.DataFrame(information)
    df.to_excel('EgyptProPlayers.xlsx',index=False)
# call user input
user_input()
# end message
print("Done! \n Data collected (needs cleaning) in EgyptProPlayers.csv")