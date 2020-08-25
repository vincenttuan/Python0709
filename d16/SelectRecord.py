import sqlite3

conn = sqlite3.connect('demo.db')
cursor = conn.cursor()

# 查詢 SQL
sql = 'SELECT id, n1, n2, n3, n4, n5, n6, ts FROM lotto'

cursor.execute(sql)
rows = cursor.fetchall() # 以 list 型態回傳多筆資料
for row in rows:
    for i in range(8):
        print(row[i], end='\t')
    print()