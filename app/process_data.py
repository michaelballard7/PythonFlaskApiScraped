import requests
import json
from bs4 import BeautifulSoup

listy = []
clean = []

def getData():
    r = requests.get("https://api.coinmarketcap.com/v1/ticker/bitcoin")
    code = r.status_code
    return r.json()

def coin_process():
    data = getData()
    coinName = data[0]["id"]
    coinSymbol = data[0]
    currentPrice = data[0]["price_usd"]
    return data

def get_eodData():
    url = 'http://eoddata.com/symbols.aspx'
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36(KHTML, like Gecklo) Chrome/56.0.2924.87 Safari/537.36',
    'referrer': 'https://google.com'}
    r = requests.get(url, headers=headers)
    html = r.text.strip()
    return html

def eod_process():
    data = get_eodData()
    soup = BeautifulSoup(data, 'lxml')
    table = soup.find(class_="quotes")
    text = table.findAll("tr")
    for x in text:
        listy.append(x.get_text())


def eod_test():
    data = get_eodData()
    soup = BeautifulSoup(data, 'html.parser')
    table = soup.table
    return table

def split_data(listy):
    dirty = []
    i = 0
    while i < len(listy):     
        for x in range(0,8):
            dirty.append(listy[x])
        clean.append('?'.join(dirty))
        i+=1



# eod_process()
# split_data(listy)
# print(clean[0].split("?")[1])
