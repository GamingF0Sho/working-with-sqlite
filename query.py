import sqlite3 as sq
conn = sq.connect('factbook.db')

c = conn.cursor()
query = "select name from facts order by population asc limit 10;"
low_population = c.execute(query).fetchall()

if __name__ == "__main__":
    print(low_population)
