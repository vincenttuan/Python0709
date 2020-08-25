import sqlite3

conn = sqlite3.connect('demo.db')
cursor = conn.cursor()

# 表格欄位名稱(Table Meta-info)
cursor.execute('PRAGMA TABLE_INFO({})'.format('lotto'))
metainfo = cursor.fetchall()
print('metainfo:', metainfo)
names = [t[1] for t in metainfo] # id, n1, n3 ....
print('names:', names)
for name in names:
    print(name, end='\t')

print('\n-----------------------------------------------')
# 查詢 SQL
sql = 'SELECT id, n1, n2, n3, n4, n5, n6, ts FROM lotto'

cursor.execute(sql)
rows = cursor.fetchall() # 以 list 型態回傳多筆資料
for row in rows:
    for i in range(8):
        print(row[i], end='\t')
    print()