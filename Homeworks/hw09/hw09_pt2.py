"""
HW9 DSC20 Winter 2019
Name of Student: Weijie Cheng
PID of Student: A14901005
"""

# Part 2. Back to basics.


import numpy as np
import pandas as pd
from datetime import *


table1 = pd.read_csv('data1.csv')
table2 = pd.read_csv('data2.csv')

def change_one(table):
    """
    changes the first table into a table with all the dates comebined
    together
    >>> table1 = pd.read_csv('data1.csv')
    >>> change_one(table1)
    [datetime.date(2013, 6, 2), datetime.date(2013, 7, 23), \
    datetime.date(2017, 9, 30), datetime.date(2017, 12, 12)]
    """
    month = table.Month.tolist()
    day = table.Day.tolist()
    year = table.Year.tolist()
    date = []
    final_date = []
    for i in range(len(month)):
        date.append(str(day[i]) + '/' + str(month[i]) + '/' + str(year[i]))
    for i in range(len(month)):
        d = pd.to_datetime(date[i], format='%d/%m/%Y').date()
        final_date.append(d)
    return final_date

def change_two(table):
    """
    changes the second table into a table with all the dates comebined
    together
    >>> table2 = pd.read_csv('data2.csv')
    >>> change_two(table2)
    [datetime.date(2015, 1, 2), datetime.date(2016, 3, 21), \
    datetime.date(2017, 5, 30), datetime.date(2018, 7, 15)]
    
    """
    month = table.Month.tolist()
    day = table.Day.tolist()
    year = table.Year.tolist()
    date = []
    final_date = []
    for i in range(len(month)):
        date.append(str(day[i]) + '/' + str(month[i]) + '/' + str(year[i]))
    for i in range(len(month)):
        d = pd.to_datetime(date[i], format='%d/%B/%Y').date()
        final_date.append(d)
    return final_date
    
# def ultimate(dataFrame):
#     return dataFrame.strftime(format = '%d-%b-%y')

change_one(table1)
table1['Date'] = change_one(table1)
table1.sort_index(ascending=False)

change_two(table2)
table2['Date'] = change_two(table2)
table2.sort_index(ascending=False)

table3 = pd.concat([table1, table2], sort=True)
table3 = table3.sort_values(by='Date', ascending=False)
df1 = table3[['Date','Tweet']]
df1.to_csv('combined.csv')
