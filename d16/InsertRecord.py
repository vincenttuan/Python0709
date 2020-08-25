import sqlite3

sql = 'INSERT INTO lotto(n1, n2, n3, n4, n5, n6) VALUES(1, 2, 3, 4, 5, 6)'

conn = sqlite3.connect('demo.db')
cursor = conn.cursor()
cursor.execute(sql)
print('取得此筆的id:', cursor.lastrowid)
conn.commit()
conn.close()
