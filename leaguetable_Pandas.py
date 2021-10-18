import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.skysports.com/premier-league-table'
html_text = requests.get(url).text
soup =BeautifulSoup(html_text,'html.parser')
players_list = soup.findAll('tr', {'class':'standing-table__row'})
list_1 =[]
for data in players_list:
    try :
        name = data.find('td', {'class':'standing-table__cell--name'}).text.strip()
        points = data.find('td', {'class': 'standing-table__cell is-hidden--bp35'}).text
        #print(name, points)
        dict={
            "Country_name": name,
            "            Points": points
        }
        list_1.append(dict)
        list_1 = list(map(lambda a: a.strip(), list_1))
    except:
        pass
#print(list_1)

df =pd.DataFrame(list_1)
print(df)



