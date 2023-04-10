import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page='

for page in range(1, 3):  # Extracting data from first two pages
    response = requests.get(url + str(page))
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'type_2'})
    rows = table.find_all('tr')[1:]  # Skipping the header row

    for row in rows:
        cols = row.find_all('td')
        rank = cols[0].get_text().strip()
        try:
            name = cols[1].select_one('a').get_text().strip()
        except AttributeError:
            name = 'N/A'

        price = cols[2].get_text().strip()
        market_cap = cols[6].get_text().strip()
        print(f"{rank} - {name} - {price} - {market_cap}")
