import requests
import pandas as pd
html_txt=requests.get('https://en.wikipedia.org/wiki/Land_speed_record', 'html.parser').text
df = pd.read_html(html_txt)
print(df[0],df[2], df[3])

df[0].to_csv('wikipedia.csv')
