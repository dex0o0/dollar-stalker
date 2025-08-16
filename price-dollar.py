import requests
from bs4 import BeautifulSoup

url = "https://www.tgju.org/profile/price_dollar_rl"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
dollar_price = soup.find('span', {'class': 'value'}).text

print(f"قیمت لحظه‌ای دلار: {dollar_price} تومان")