# 資料的轉換
x = input('請輸入一個數字 x : ')
y = input('請輸入一個數字 y : ')
print(x, y)
sum = x + y
print(sum)
# 觀察 x, y 的資料型態
print(x, type(x), y, type(y))
# 經觀察結果發現 x, y 都是 str 字串
# 所以要透過 int(字串變數) 來進行字串轉數字的程序
sum = int(x) + int(y)
print(sum)