import sqlite3 as sq
import pandas as pd
import math

conn = sq.connect('factbook.db')

query_al = "select sum(area_land) from facts;"
al_total = pd.read_sql_query(query_al, conn).dropna(axis=0)
al = int(al_total.loc[0])

query_aw = "select sum(area_water) from facts;"
aw_total = pd.read_sql_query(query_aw, conn).dropna(axis=0)
aw = int(aw_total.loc[0])

al_aw_ratio = al / aw

if __name__ == "__main__":
    print(al_aw_ratio)
