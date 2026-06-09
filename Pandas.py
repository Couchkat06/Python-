"""Pandas- python library built on top of numpy
(Panel Data, not pandas the animal)
Series (1 dim) vs Dataframes (2 dim)
"""

import pandas as pd

print(pd.__version__)

data = [100, 102, 104]

series = pd.Series(data, index = ["a", "b", "c"]) #default index = 0

series.loc["a"] #access appropriate value

print(series.loc["a"]) #data type changes based on data set
#index and series length must match

print(series[series >= 200])


calories = {"Day 1" : 1750, "Day 2" : 2100, "Day 3": 1700}

series = pd.Series(calories)

print(series.loc["Day 3"])

print(series[series > 1800])

print(series.loc["Day 3"])

#Dataframe = A tabular data strcuture with rows AND columns. (2 dimensional) 
#Similar to an Excel Spreadsheet

data = {"Name": ["Spongebob", "Patrick", "Squidward"],
        "Age": [30, 35, 50]
}

df = pd.DataFrame(data, index = ['Employee 1', "Employee 2", "Employee 3"])

#add a new column
df["Job"] = ["Cook", "N/A", "Cashier"]

#Add a new row
new_row = pd.DataFrame([{"Name" : "Sandy", 'Age': 28, "Job": "Engineer"},
                        {"Name": "Eugene", "Age": 60, "Job": "Manager"}],
                        index = ["Employee 4", "Employee 5"])

df = pd.concat([df, new_row]) #save the new row info to a variable, then concat it to the dataframe

print(df)

#Importing CSV (Comma Separated Values) and JSON (Javascript Object Notation)

df = pd.read_csv("Original150pokemons")
