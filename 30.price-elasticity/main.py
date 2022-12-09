import pandas as pd

# Creating a dataset
data = pd.DataFrame({"Demand": [20, 30, 31, 33, 30, 33, 35],
                     "Price": [2000, 1800, 1850, 1700, 1800, 1700, 1600]})


# Finding change in Demand, Price
data["Change in Demand"] = data["Demand"].pct_change()
data["Change in Price"] = data["Price"].pct_change()


# Finding price elasticity
data["Price elasticity"] = data["Change in Demand"] / data["Change in Price"]

print(data)
