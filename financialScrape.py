from bs4 import BeautifulSoup
import requests
import re

symb = input("Please enter stock symbol >> ")

def finScrape(symbol):
    scrap = requests.get("https://www.marketwatch.com/investing/stock/" + symbol + "/financials")
    soup = BeautifulSoup(scrap.content, 'html.parser')

    values = soup.findAll('td',{"class": 'valueCell'})
    titles = soup.findAll('td',{'class': 'rowTitle'})

    scrapeData = ["Measure", "2015", "2016", "2017", "2018", "2019"]

    q = 0
    for i in titles:
        scrapeData.append(str(re.sub(re.compile('<.*?>'), '', str(i))).strip())
        for x in range(q, q+5):
            scrapeData.append(str(re.sub(re.compile('<.*?>'), '', str(values[x]))).strip())
        q = q + 5

    for i in range(len(scrapeData)):
        if (i % 6 == 0):
            print(scrapeData[i]+" "+scrapeData[i+1]+" "+scrapeData[i+2]+" "+scrapeData[i+3]+" "+scrapeData[i+4]+" "+scrapeData[i+5])

finScrape(symb)