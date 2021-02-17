from selenium import webdriver
from bs4 import BeautifulSoup
import re
from collections import Counter
import pandas as pd
driver = webdriver.Chrome()
team = []
games = []
teams = {}
driver.get("https://www.espn.com/nba/schedule/_/date/20210217")
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
for a in soup.findAll('a', attrs={'class': 'team-name'}):
    name = a.find('span')
    team.append(name.text)
teams = Counter(team)

print(teams)
#df = pd.DataFrame(list(teams.items()))
df = pd.DataFrame.from_dict(teams, orient='index').reset_index()
df = df.rename(columns={'index':'team name', 0:'games'})
df.to_csv('teams.csv', index=False, encoding='utf-8')
