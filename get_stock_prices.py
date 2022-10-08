import requests
from bs4 import BeautifulSoup
import json

my_stocks = [ "MCD", "SBUX", "NKE", "WMT", "AAPL", "MSFT" ]
stock_data = []

def get_data(symbol):
    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
    url = f"https://finance.yahoo.com/quote/{symbol}?p={symbol}"

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    stock = {
    "price": soup.find("div", { "class": "D(ib) Mend(20px)"}).find_all("fin-streamer")[0].text,
    "changeAmount": soup.find("div", { "class": "D(ib) Mend(20px)"}).find_all("span")[0].text,
    "change": soup.find("div", { "class": "D(ib) Mend(20px)"}).find_all("span")[1].text
    }
    return stock

for item in my_stocks:
    stock_data.append(get_data(item))
    print("Getting: ", item)

with open("stockdata.json", "w") as file:
    json.dump(stock_data, file)