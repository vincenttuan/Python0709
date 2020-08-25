import sqlite3

db = sqlite3.connect('demo.db')
print(db)
db.close()
