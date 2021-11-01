from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()

name = []
rating = []
driver.get("https://www.imdb.com/chart/top/")

content = driver.page_source
soup = BeautifulSoup(content)

for a in soup.findAll('td', attrs={'class': 'titleColumn'}):
    name.append(str(a.text).strip())

for b in soup.findAll('td', attrs={'class': 'ratingColumn imdbRating'}):
    rating.append(str(b.text).strip())

df = pd.DataFrame({'Movie Name': name, 'Rating': rating })
df.to_csv('movies.csv', index=False, encoding='utf-8')