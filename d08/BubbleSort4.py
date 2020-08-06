def sort(rows, flag=True):
    for i in range(0, len(rows)):
        for j in range(i + 1, len(rows)):
            x = rows[i]
            if flag:
                if rows[i] > rows[j]:
                    rows[i] = rows[j]
                    rows[j] = x
            else:
                if not rows[i] > rows[j]:
                    rows[i] = rows[j]
                    rows[j] = x
    return rows

if __name__ == '__main__':
    rows = [3, 8, 5, 7, 2]
    rows = sort(rows)
    print(rows)
    rows = sort(rows, False)
    print(rows)
