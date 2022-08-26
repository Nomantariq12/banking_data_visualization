#!/usr/bin/env python
# coding: utf-8

# # Visualizing Data of Banks

# In[1]:


# importing Liabraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


# Styling for Graphs
plt.style.use("fivethirtyeight")


# # Investment in PIB's as a Proportion of their own invsetment portfolio

# In[7]:


# Different Bank Data
dic = {
    "bop": [14, 0, 58, 38, 71],
    "hbl": [45, 29, 45, 53, 60],
    "mcb": [34, 16, 39, 35, 61],
    "ubl": [48, 48, 30, 20, 21],
    "bahl": [25, 20, 37, 68, 65],
    "bafl": [36, 19, 43, 39, 53],
    "abl": [34, 9, 20, 49, 51],
    "hmb": [39, 42, 36, 35, 32],
    "nbp": [24, 28, 35, 44, 47],
    "akbl": [49, 38, 43, 63, 51],
    "bok": [58, 69, 45, 55, 30],
    "jsbl": [90, 62, 57, 36, 35],
    "snbl": [48, 28, 32, 52, 53],
    "scbl": [0, 0, 8, 44, 34],
    "sbl": [22, 38, 90, 91, 96],
}

# Converting Dictionary Data into Pandas DataFrame
data = pd.DataFrame(dic)

# X-axis data for bar plot, which is just counting of total number of banks we have.
x = np.arange(len(data.columns))

# setting the width of the bar plot
width = 0.17

# Defining Size of Diagrams
plt.rcParams["figure.figsize"] = (50, 10)

#Bar Plot for Year 2017
plt.bar(x - (width * 2), data.iloc[0,:], width=width, label="2017")
#This is the representation of percetagne above each bar plot.
for i in range(len(x)):
    plt.text(i - (width * 2), data.iloc[0,i]+1, str(data.iloc[0, i]) + "%", ha="center", va="baseline",
            color="darkblue")

#Bar Plot for Year 2018
plt.bar(x - width, data.iloc[1,:], width=width, label="2018")
#This is the representation of percetagne above each bar plot.
for i in range(len(x)):
    plt.text(i - width, data.iloc[1,i]+1, str(data.iloc[1, i]) + "%", ha="center", va="baseline", 
            color="red")

#Bar Plot for Year 2019
plt.bar(x, data.iloc[2, :], width=width, label="2019")
#This is the representation of percetagne above each bar plot.
for i in range(len(x)):
    plt.text(i, data.iloc[2,i]+1, str(data.iloc[2, i]) + "%", ha="center", va="baseline")

#Bar Plot for Year 2020
plt.bar(x + width, data.iloc[3, :], width=width, label="2020")
#This is the representation of percetagne above each bar plot.
for i in range(len(x)):
    plt.text(i + width, data.iloc[3, i]+1, str(data.iloc[3,i]) + "%", ha="center", va="baseline", 
             color="green")

#Bar Plot for Year 2021
plt.bar(x + (width * 2), data.iloc[4, :], width=width, label="2021")
for i in range(len(x)):
    plt.text(i + (width * 2), data.iloc[4,i]+1, str(data.iloc[4,i])+"%", ha="center", va="baseline",
            color="grey")

plt.legend(loc=(0.4, 0.9), ncol=5)
# Title, and x-axis labels
plt.title("Investment in PIB's as a Proportion of their own investment portfolio", loc="left")
plt.xlabel("Bank")
# Replacing x Values(that are just numbers) to Bank Names
plt.xticks(x, data.columns.str.upper())
plt.savefig("Investment_In_PIB's.png")
plt.show()


# ===================================================================================================================

# # Investment in t-bills as a Proportion of their own investment portfolio

# In[4]:


# Different Bank Data
dic1 = {
    "bop": [81, 94, 39, 58, 24],
    "hbl": [37, 55, 42, 32, 20],
    "mcb": [58, 76, 53, 58, 31],
    "ubl": [35, 29, 29, 30, 35],
    "bahl": [69, 72, 51, 19, 15],
    "bafl": [47, 58, 35, 37, 15],
    "abl": [56, 81, 75, 43, 43],
    "hmb": [52, 49, 59, 59, 61],
    "nbp": [63, 58, 47, 43, 42],
    "akbl": [41, 48, 42, 27, 39],
    "bok": [33, 17, 57, 25, 50],
    "jsbl": [13, 30, 52, 57, 59],
    "snbl": [45, 66, 60, 41, 41],
    "scbl": [98, 97, 92, 40, 62],
    "sbl": [25, 56, 0, 0, 1],
}
dic1

# Converting Dictionary Data into Pandas DataFrame
data1 = pd.DataFrame(dic1)

# X-axis data for bar plot, which is just counting of total number of banks we have.
x1 = np.arange(len(data1.columns))
x1

# setting the width of the bar plot
width = 0.17

# Defining Size of Diagrams
plt.rcParams["figure.figsize"] = (50, 10)

#Bar Plot for Year 2017
plt.bar(x1 - (width * 2), data1.iloc[0,:], width=width, label="2017")
#This is the representation of percetagne above each bar plot.
for i in range(len(x)):
    plt.text(i - (width * 2), data1.iloc[0,i]+1, str(data1.iloc[0, i]) + "%", ha="center", va="baseline",
            color="darkblue")

#Bar Plot for Year 2018
plt.bar(x1 - width, data1.iloc[1,:], width=width, label="2018")
#This is the representation of percetagne above each bar plot.
for i in range(len(x)):
    plt.text(i - width, data1.iloc[1,i]+1, str(data1.iloc[1, i]) + "%", ha="center", va="baseline", 
            color="red")

#Bar Plot for Year 2019
plt.bar(x1, data1.iloc[2, :], width=width, label="2019")
#This is the representation of percetagne above each bar plot.
for i in range(len(x)):
    plt.text(i, data1.iloc[2,i]+1, str(data1.iloc[2, i]) + "%", ha="center", va="baseline")

#Bar Plot for Year 2020
plt.bar(x1 + width, data1.iloc[3, :], width=width, label="2020")
#This is the representation of percetagne above each bar plot.
for i in range(len(x)):
    plt.text(i + width, data1.iloc[3, i]+1, str(data1.iloc[3,i]) + "%", ha="center", va="baseline", 
             color="green")

#Bar Plot for Year 2021
plt.bar(x1 + (width * 2), data1.iloc[4, :], width=width, label="2021")
for i in range(len(x)):
    plt.text(i + (width * 2), data1.iloc[4,i]+1, str(data1.iloc[4,i])+"%", ha="center", va="baseline",
            color="grey")

plt.legend(loc=(0.4, 0.9), ncol=5)
# Title, and x-axis labels
plt.title("Investment in t-bills as a Proportion of their own investment portfolio", loc="left")
plt.xlabel("Bank")
# Replacing x Values(that are just numbers) to Bank Names
plt.xticks(x, data.columns.str.upper())
plt.savefig("Investment_In_tbills.png")
plt.show()


# ==============================================================================================================

# # Advances to Deposits Ratio Visualization 

# In[5]:


#Bank Data
banks = ["sbl", "jsbl", "bahl", "mebl", "bok", "bafl", "hbl", "hmb", "mcb", "akbl", "abl", "bop", "ubl", "fabl",
        "scbpl", "snbl", "nbp"]
bank = [i.upper() for i in banks]

diff_bet_2021_and_2012 = [29, 23, 12, 12, 10, 7, 2, 0, 0, -3, -9, -13, -14, -15, -19, -26, -27]

# Defining Size of Diagrams
plt.rcParams["figure.figsize"] = (20, 10)

width1 = 0.5

# Bar Plot for Differnt Banks
plt.bar(bank, diff_bet_2021_and_2012, color="#04396D", width=width1)
for i in range(len(banks) // 2):
    plt.text(i, diff_bet_2021_and_2012[i]-1, str(diff_bet_2021_and_2012[i])+"%",
            va="center",
            ha="center",
            color="white")
for y in range(len(banks) // 2 + 1, len(banks)):
    plt.text(y, diff_bet_2021_and_2012[y]+1, str(diff_bet_2021_and_2012[y])+"%",
            va="center",
            ha="center",
            color="white")
plt.text(7, -1, "0%", color="black", va="center", ha="center")
plt.text(8, -1, "0%", color="black", va="center", ha="center")

plt.title("Change in Bank Strategy - Advances to Deposits Ratio", loc="left")
plt.ylabel("Difference between 2021 and 2012")
plt.xlabel("Bank")
plt.savefig("Advances_to_Deposits Ratio.png")
plt.show()


# ===================================================================================================================

# # Investment to Deposit Ratio

# In[6]:


invest_to_dep_ratio = [79, 32, 31, 31, 30, 24,22, 19,12,8, 7,4, -5,-8,-10, -23, -23]
raw_data = "sbl snbl nbp ubl bafl abl scbpl fabl hmb akbl bok bop mcb hbl bahl jsbl mebl"
banks = raw_data.upper().split(" ")

# Defining Size of Diagrams
plt.rcParams["figure.figsize"] = (20, 10)

width1 = 0.5

# Bar Plot for Differnt Banks
plt.bar(banks, invest_to_dep_ratio, color="#04396D", width=width1)
for i in range(12):
    plt.text(i, invest_to_dep_ratio[i]-2, str(invest_to_dep_ratio[i]) + "%",
            va="center",
            ha="center",
            color="white")
for y in range(12, len(banks)):
    plt.text(y, invest_to_dep_ratio[y]+2, str(invest_to_dep_ratio[y])+"%",
            va="center",
            ha="center",
            color="white")
    
plt.title("Change in Bank Strategy - Investment to Deposit Ratio", loc="left")
plt.ylabel("Difference between 2021 and 2012")
plt.xlabel("Bank")
plt.savefig("Investment_to_dep_ratio.png")
plt.show()


# In[ ]:




