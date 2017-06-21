import sqlite3
import os

dname = 'test.db'

if os.path.exists(dname):
    os.remove(dname)

conn = sqlite3.connect(dname) 
c = conn.cursor()

c.execute('''CREATE TABLE database
(d1 text,d2 int, d3 real)''')

c.execute("INSERT INTO database VALUES ('data1',10,3.14)")

conn.commit()

c.execute("SELECT * FROM database")
r = c.fetchone() # 返却値の型はtupleだった
print(r)