import sqlite3
import pandas as pd

conn = sqlite3.connect('factbook.db')
c = conn.cursor()
query = '''
    SELECT SUM(area_land),SUM(area_water) FROM facts
    WHERE area != ''
    '''
c.execute(query)
data = c.fetchall()
ratio = data[0][0]/data[0][1]
print(ratio)
conn.close()
