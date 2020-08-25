
def menu():
    print('1.建立表單')
    print('2.新增紀錄')
    print('3.全部查詢')
    print('4.單筆查詢')
    print('5.修改紀錄')
    print('6.刪除紀錄')
    print('9.離開系統')
    print('-----------')
    n = int(input('請選擇: '))
    if n == 9:
        return
    else:
        choice(n)
    menu()

def choice(n):
    if n == 1:
        createTable()
    elif n == 2:
        insertRecord()
    elif n == 3:
        selectAllRecords()
    elif n == 4:
        selectRecord()
    elif n == 5:
        updateRecord()
    elif n == 6:
        deleteRecord()

def createTable():
    pass

def insertRecord():
    pass

def selectAllRecords():
    pass

def selectRecord():
    pass

def updateRecord():
    pass

def deleteRecord():
    pass

if __name__ == '__main__':
    menu()