ttt = [['O', 'O', 'X'],['X', 'O', ' '],['X', ' ', 'X']]
for row in ttt:
    print(row)

#如何讓 O 贏 ?
n = int(input('請輸入位置0~8:'))
ttt[n//3][n%3] = 'O'
for row in ttt:
    print(row)