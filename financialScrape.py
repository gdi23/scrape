from bs4 import BeautifulSoup
import requests
import re
import numpy as np
import pandas as pd

symb = input("Please enter stock symbol >> ")

def finScrape(symbol):
    scrap = requests.get("https://www.marketwatch.com/investing/stock/" + symbol + "/financials")
    soup = BeautifulSoup(scrap.content, 'html.parser')

    values = soup.findAll('td',{"class": 'valueCell'})
    titles = soup.findAll('td',{'class': 'rowTitle'})

    scrapeData = np.array([["Measure", "2015", "2016", "2017", "2018", "2019"]])
    
    q = 0
    for i in titles:
        data = []
        data.append(str(re.sub(re.compile('<.*?>'), '', str(i))).strip())
        for x in range(q, q+5):
            data.append(str(re.sub(re.compile('<.*?>'), '', str(values[x]))).strip())
        data = [data]
        scrapeData = np.append(scrapeData,data,axis=0)
        q = q + 5
    scrapeData = pd.DataFrame(data=scrapeData[1:,1:], index=scrapeData[1:,0], columns=scrapeData[0,1:])

    print(scrapeData)

finScrape(symb)