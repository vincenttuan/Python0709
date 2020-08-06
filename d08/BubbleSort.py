rows = [3, 8, 5, 7, 2]
#       0  1  2  3  4

for i in range(0, len(rows)):
    for j in range(i+1, len(rows)):
        x = rows[i]
        if rows[i] > rows[j]:
            rows[i] = rows[j]
            rows[j] = x

print(rows)