import sqlite3
import pandas as pd
import math
conn = sqlite3.connect('factbook.db')
c = conn.cursor()
query = 'SELECT name,population,population_growth FROM facts'
data = pd.read_sql_query(sql=query, con=conn)
data = data.dropna()

def p_final(df):
    p = df['population']
    pg = df['population_growth']
    n = p * (math.e**(35*pg))
    return n

data['pplt_final'] = data.apply(p_final, axis=1)
data.sort_values(by='pplt_final', ascending=False, axis=0, inplace=True)
print(data)

conn.close()