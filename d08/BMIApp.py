import d08.BubbleSort3 as bb

rows = [{'h':170, 'w':60},
        {'h':160, 'w':55},
        {'h':180, 'w':70},]

#rows = bb.sort('h', rows)
#rows = bb.sort('w', rows)
# 根據 bmi 來排序
for row in rows:
    w = row.get('w')
    h = row.get('h')
    bmiValue = w/(h/100)**2
    row.setdefault('bmi', bmiValue)

rows = bb.sort('bmi', rows)
print(rows)


