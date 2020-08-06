# 加法的方法
def add(x, y):
    print("執行到 add() 方法", x, y)
    result = x + y
    return result

# 訊息說明方法
def info():
    print("執行到 info() 方法")
    print("本程式事由 Python 所撰寫")
    #return

# 判斷性別
# A155556666
def checkSex(id):
    sex = id[1]
    if sex == '1':
        print("男性")
        return
    if sex == '2':
        print("女性")
        return


    # 主程式
sum = add(10, 20)
print(sum)
info()
checkSex('A233334444')