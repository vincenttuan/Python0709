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
    sql = open('data.sql', 'r').read()
    conn.execute(sql)
    conn.commit()
    print('資料表建立成功!')

def insertRecord():
    name = input('請輸入姓名:')
    age = int(input('請輸入年齡:'))
    sex = int(input('請輸入性別(1:男, 2:女):'))
    sql = 'INSERT INTO student(name, age, sex) VALUES("%s", %d, %d)' % (name, age, sex)
    cursor = conn.execute(sql)
    print('新增成功, id=', cursor.lastrowid)
    conn.commit()

def selectAllRecords():
    sql = "SELECT id, name, age, sex, ts FROM student"
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        for i in range(5):
            print(row[i], end='\t')
        print()

def selectRecord():
    pass

def updateRecord():
    id = int(input('請輸入要修改的 id 號碼:'))
    flag = input('是否要修改姓名(y/n)?')
    if flag == 'y':
        name = input('請輸入姓名:')
        sql = 'UPDATE student SET name="%s" WHERE id=%d' % (name, id)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        print('修改姓名成功!')
    flag = input('是否要修改年齡(y/n)?')
    if flag == 'y':
        age = int(input('請輸入年齡:'))
        sql = 'UPDATE student SET age=%d WHERE id=%d' % (age, id)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        print('修改年齡成功!')
    flag = input('是否要修改性別(y/n)?')
    if flag == 'y':
        sex = int(input('請輸入性別(1:男, 2:女):'))
        sql = 'UPDATE student SET sex=%d WHERE id=%d' % (sex, id)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        print('修改性別成功!')

def deleteRecord():
    pass

if __name__ == '__main__':
    menu()
    conn.close()