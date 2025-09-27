import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

url = "https://www.bcci.tv/international/men/stats/test"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
div = soup.find('div', class_='stats-data-table-player') 

table = div.find('table', class_='table')

header = ['Rank','Name', 'Matches', 'Inns', 'Avg', 'SR', 'HS', 'Fours', 'Sixs', 'Fifty', 'Century', 'Runs']
rows = []         


for row in table.find_all('tr'):
    data_elements = row.find_all(['h5','p', 'h6'])

    if data_elements:
        player_stats = [el.text.strip() for el in data_elements]
        if len(player_stats) == 12: 
            rows.append(player_stats)


print("Header:", header)
print("Rows:", rows)        

with open('bcci_batting_test.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(header)  
    # writer.writerow(rows)
    for row in rows:
        writer.writerow(row)





