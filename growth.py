import sqlite3 as sq
import pandas as pd
import math

conn = sq.connect('factbook.db')

query = "select * from facts;"
facts_db = pd.read_sql_query(query, conn).dropna(axis=0)

def pop_growth(row):
    init_pop = row['population']
    r35 = row['population_growth'] * 35
    x = math.e
    end_pop = init_pop * x ** r35
    return end_pop

facts_db['pop_2050'] = facts_db.apply(pop_growth, axis=1)
pop_2050_db = facts_db.sort_values('pop_2050', ascending=True)
pop_2050_reindexed = pop_2050_db.reset_index(drop=True)
pop_2050_top10 = pop_2050_reindexed['name'].head(10)
    
pop = facts_db.sort_values('population', ascending=False)    

test = facts_db['population'][1] ** 2

if __name__ == "__main__":
    print(pop_2050_top10)