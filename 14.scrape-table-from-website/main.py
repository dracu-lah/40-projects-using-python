import urllib.request
import pandas as pd
url="https://www.w3schools.com/html/html_tables.asp"

with urllib.request.urlopen(url) as i:
    html = i.read()
data = pd.read_html(html)[0]
print(data.head())