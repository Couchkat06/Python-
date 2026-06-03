#matplotlib

import matplotlib.pyplot as plt
import numpy as np

#putting things in terms of arrays is faster 
x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([17, 23,28, 5 ])
y3 = np.array([12, 15, 20, 30])

line_style = dict(marker = "*", # period for box, o for circle, v for triangle
                    marketsize = 20, #markersize can also be written as ms
                    markerfacecolor = "1cd3fc",
                    markeredgecolor = "#1cd3fc", #can type in color name or hex codes
                    linestyle = "dotted",
                    linewidth = 2,
                    color = "#1c5bfc") 

plt.title("Class Size", fontsize = 25,
                        family = "Arial",
                        fontweight = "bold",
                        color = "#2d4cfc")

plt.xlabel("Year", fontsize = 20,
                   family = "Arial",
                   fontweight = "bold",
                   color = "2dbefc")

plt.ylabel("Students", fontsize = 20,
                   family = "Arial",
                   fontweight = "bold",
                   color = "2dbefc")

plt.tick_params(axis = "both",
                colors = "2dbefc")

#plot customization
plt.plot(x, y1, **line_style)
plt.plot(x, y2, **line_style)
plt.plot(x, y3, **line_style)
#plots all 3 lines

plt.xticks(x)

plt.show()   #show the plot

#grid lines
#grid() = Helps make plots easier to read by adding reference lines

x2 = [1, 2, 3, 4]
y0 = [5, 10, 15, 20, 25]

plt.grid(axis = "y",
         linewidth = 3,
         color = "lightgray",
         linestyle = "dashdot")

plt.plot(x2, y0)
plt.show()

#Bar Chart = compare categories of data by representing each category with a bar 

categories = np.array([" Grains", "Fruit", "Vegetables", "Protein", "Dairy", "Sweets"])
values = np.array([4, 3, 2, 5, 3, 1])

plt.bar(categories, values, color = "skyblue")
#plt.barh(categories, values, color = "skyblue") - makes the bar chart horizontal

plt.title("Daily Consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")

plt.show()

#Pie Chart = circular chart divided into slices to show percentages of the total
#Good for visualizing distribution among categories.

categories = ["Freshmen", "Sophomores", "Juniors", "Seniors"] #list of strings don't really benefit from arrays
values = np.array([300, 250, 275, 225])
colors = ["red", "blue", "yellow", "green"]

plt.pie(values, labels = categories, 
                autopct = "%1.1f%%", #data labels
                colors = colors,
                explode = [0, 0, 0 ,0.1], #makes the slices shift out 
                shadow = True,
                startangle = 90)
 

plt.show()

"""Scatter graph = Shows the relationship between 2 variables
                    Helps to identify a correlation (+, - , None)
                    Example: Study Hours vs Test Scores

"""

x1 = np.array([0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8]) #Hours studied
y1 = np.array([55, 60, 65, 62, 68, 70, 75, 78, 82, 85, 87]) #Grades


x2 = np.array([0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 8]) #Hours studied
y2 = np.array([50, 58, 65, 70, 72, 78, 83, 88, 92, 95, 97]) #Grades


plt.scatter(x1, y1, color = "skyblue",
                    alpha = 0.5, #transparency, 0.1 = 10%
                    s = 200, #s = size
                    label = "Class 1")

plt.scatter(x2, y2, color = "red",
                    alpha = 0.5, #transparency, 0.1 = 10%
                    s = 200, #s = size
                    label = "Class 2")


plt.title("Test Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Grade") 

plt.legend() 
plt.show()


"""Histograms = A visual representation of the distribution of the quantitative data
                They group values into bins (intervals)
                and counts how many fall in each range
"""

scores = np.random.normal(loc = 80, #center/mean of distribution
                          scale = 10, #sd of distribution
                          size = 100 #number of values
                          )

scores = np.clip(scores, 0, 100) #setting min and max bounds

plt.hist(scores, bins= 10,
                 color = "lightgreen",
                 edgecolor = "black")

plt.title('Exam Scores')
plt.xlabel("Score")
plt.ylabel("# of Students")

plt.show()

#Subplots

#Figure = the entire canvas for which we add plots to
#Ax = a single plot (subplot)

figure, axes = (plt.subplot(2, 2)) #axes = technically a numpy array

axes[0,0].plot(x, x*2, color = "red")
axes[0,0].set_title("x*2")

axes[0,1].bar(x, x**2, color = "blue")
axes[0,1].set_title("x**2")

axes[1,0].plot(x, x**3, color = "green")
axes[1,0].set_title("x**3")

axes[1,1].plot(x, x**4, color = "purple")
axes[1,1].set_title("x**4")

plt.tight_layout() #makes all subplots fit, no overlap
plt.show()

#matplotlib + pandas ->

import pandas as pd

#df assigns file to a dataframe
df = pd.read_csv("Original150pokemons.csv")



print(df["Type1"]) #only prints a single column/series under Type1
print(df["Type1"].value_counts()) #Counts how many are under each Type

type_count = df["Type1"].value_counts(ascending = True)

plt.barh(type_count.index, type_count.values, color = "03dffc",edgecolor = "Black") # (type, # in each type)

plt.title("# of Pokemon by Primary Type")
plt.xlabel("Count")
plt.ylabel("Type")
plt.tight_layout()

plt.show()