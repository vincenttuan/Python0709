import sqlite3
import random

conn = sqlite3.connect('demo.db')
cursor = conn.cursor()

lottos = []

for i in range(100):
    # 取出 1~49 不重複的數字共6個
    nums = set()
    while len(nums) < 6:
        nums.add(random.randint(1, 46))
    lottos.append(tuple(nums)) # 要轉成元組(資料庫規定)

print(lottos)

# 多筆資料新增
cursor.executemany('INSERT INTO lotto(n1, n2, n3, n4, n5, n6) VALUES(?, ?, ?, ?, ?, ?)', lottos)
conn.commit()
conn.close()
print('新增多筆資料成功')