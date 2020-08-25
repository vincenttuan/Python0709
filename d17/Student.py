import sqlite3

conn = sqlite3.connect('school.db')

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
    sql = 'CREATE TABLE if not exists "student" ('\
	      '"id" INTEGER,'\
	      '"name" TEXT NOT NULL,'\
	      '"age" INTEGER NOT NULL,'\
	      '"sex" INTEGER NOT NULL,'\
	      '"ts" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,'\
	      'PRIMARY KEY("id" AUTOINCREMENT)'\
          ')'
    conn.execute(sql)
    conn.commit()
    print('資料表建立成功!')

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
    conn.close()