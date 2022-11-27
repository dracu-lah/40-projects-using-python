# pip install pandas
import pandas as pd
data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/articles.csv", encoding = 'latin1')
print(data.head())

data["Number of Words"] = data["Article"].apply(lambda n: len(n.split()))
print(data.head())