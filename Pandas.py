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

print(df.to_string()) #prints all the data in the df

#Selection by Column 
print(df["Name"].to_string()) #Passes in a column name to select that column
print(df["Height"].to_string())
print(df["Weight"].to_string())
print(df[["Name", "Height", "Weight"]].to_string())

#Selection by Rows

df = pd.read_csv("Original150pokemons", index_col = "Name")

print(df.loc["Charizard": "Blastoise", ["Height", "Weight"]]) 

print(df.iloc[0:11:2, 0:3]) #gives every second row according to the index number, gives first 3 columns
#iloc = index locate

pokemon = input("Enter a Pokemon name: ")

try: 
    print(df.loc[pokemon])
except KeyError: 
    print(f"{pokemon} not found")

#Filtering = Keeping the rows that match a condition

tall_pokemon = df[df["Height"] >= 2]
heavy_pokemon = df[df["Weight"] > 100]
legendary_pokemon = df[df['Legendary'] == True]
water_pokemon = df[(df["Type1"] == "Water") |
                   (df["Type2"] == "water")]

ff_pokemon = df[(df['Type1'] == "Fire") & 
                (df["Type3"] == "Flying")]


print(tall_pokemon)
print(heavy_pokemon)
print(water_pokemon)
print(ff_pokemon)

"""Aggregate functions = Reduces a set of values into a single summary value
    Used to summarize and analyze data
    Oftern used with the groupby() function
"""

print(df.mean(numeric_only = True)) #can only be used on columns that have numerical data
#Find mean of any columns that are numeric

print(df.sum(numeric_only = True))
print(df.min(numeric_only = True))
print(df.max(numeric_only = True))
print(df.count()) #Counts no of values in each column

#Selecting a single column
print(df["Height"].mean())
print(df['Height'].sum())
print(df["Height"].min())
print(df["Height"].max())
print(df["Height"].count()) #Counts no of values in each column

#groupby
group = df.groupby("Type1") #Grouping by Type 1

print(group["Height"].mean())
print(group["Height"].sum())
print(group["Height"].min())
print(group["Height"].max())
print(group["Height"].count())

"""Data Cleaning = Process of fixing/removing:
                    incomplete, incorrect, or irrelevant data
                    ~75% of work done with Pandas is data cleaning
"""

df = pd.read_csv("data.csv")

#1. Drop irrelevant columns
df = df.drop(columns=["Legendary", "No"])

#2. Handle missing data
df = df.dropna(subset = ["Type2"]) #Within type 2, drop any rows that are missing a value
#Any columns we place within subset list will drop those rows if they're missing a value

df = df.fillna({"Type2": "None"}) 
#fill any not available values of selected column with the dictionary value
#in this case, replace any not available values in column Type2 with "None

#3. Fix inconsistent values
df["Type1"] = df["Type1"].replace({"Grass": "GRASS",
                                   "Fire": "FIRE",
                                   "Water": "WATER"})

#4. Standardize text
df["Name"] = df["Name"].str.lower() #take name column, makes all characters lowercase

#5. Fix Data Types
df["Legendary"] = df["Legendary"].astype(bool)

#6. Remove duplicate values
df = df.drop_duplicates()

print(df.to_string())