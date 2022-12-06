# y importing the necessary Python libraries and a dataset that we can use to visualize box plots
import pandas as pd

data = pd.read_csv(
    "https://raw.githubusercontent.com/amankharwal/Website-data/master/Advertising.csv")
print(data.head())

# visualizing box plot

import plotly.express as px
fig = px.box(data, y="TV")
fig.show()
