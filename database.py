# -*- coding: utf-8 -*-
import sqlite3 as lite

con = lite.connect('challenge_one.db')

import pandas as pd

with con:
    cur = con.cursor()
    cur.execute("SELECT name, state, year, warm_month, cold_month, average_high FROM cities INNER JOIN weather ON name = city")
    rows = cur.fetchall()
    df = pd.DataFrame(rows)

df

df.to_csv(‘combined_table.csv’)

df = df.rename(columns={0: 'City', 1: 'State', 2: 'Year', 3: 'Warm_Month', 4: 'Cold_Month', 5:'Avg_High'})

msg = row['City'] + ' , ' + row['State']

for Avg_High, rows in df.iterrows():
    df[df['Warm_Month'] == 'July']
    df.index[0:2]
    print "The warmest cities in July are" + msg
