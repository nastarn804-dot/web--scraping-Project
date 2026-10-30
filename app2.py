import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore

import sqlite3
import streamlit # pyright: ignore[reportMissingImports]

url = 'https://www.technolife.com/category/mobile'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

#print(soup)

DB_NAME = 'MobileProduct.db'
conn = sqlite3.connect(DB_NAME)
print('DB CREATED')


query = '''CREATE TABLE IF NOT EXISTS MobileData
(id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
price TEXT, 
image TEXT, 
link TEXT
)
'''
cursor = conn.cursor()
cursor.execute(query)
conn.commit()
# conn.close()

print('TABLE CREATED')

cards = soup.select('section.relative.w-full.rounded-\\[10px\\].bg-white')
print(len(cards))

for card in cards:
    title = card.find('h2').text.strip()
    if title == None:
        continue

    # print(title)

    price = card.select_one('p.text-\\[22px\\].font-semiBold.leading-5').text.strip()
    if price == None:
        continue

    print(price)

    image = card.select_one('a[href^="/product-"] img').get('src')
    img_url = 'https://www.technolife.com' + image

    print(img_url)
    link = 'https://www.technolife.com' + card.select_one('a[href^="/product-"]').get('href')

    query = '''
        INSERT INTO MobileData(title, price, image, link) 
        VALUES(?, ?, ? , ?)
        '''
    cursor.execute(query, (title, price, img_url, link))
    conn.commit()

conn.close()
print('WEB DATA Scraped')