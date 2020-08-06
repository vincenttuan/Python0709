import os
import atm.Account as act
# 主程式
act1 = act.Account(1000)
act2 = act.Account(1000)
act3 = act.Account(1000)
list = [{"john": act1}, {"mary": act2}, {"tom": act3}]

# 列出所有人的帳戶餘額
def display():
    for act in list:
        for key in act.keys():
            print(key, act.get(key))

def save():
    actName = input('請輸入存款人: ')
    x = int(input('請輸入存款金額: '))
    # 得到存款人的account物件
    account = None
    for act in list:
        for key in act.keys():
            if key == actName:
                account = act.get(key)
    if account == None:
        print('查無此人')
    else:
        account.save(x)

def withdraw():
    actName = input('請輸入提款人: ')
    x = int(input('請輸入提款金額: '))
    # 得到提款人的account物件
    account = None
    for act in list:
        for key in act.keys():
            if key == actName:
                account = act.get(key)
    if account == None:
        print('查無此人')
    else:
        account.withdraw(x)

def transfer():
    fromName = input('請輸入轉帳人(from): ')
    toName   = input('請輸入被轉帳人(to): ')
    x = int(input('請輸入轉帳金額: '))
    fromAccount = None
    toAccount = None
    for act in list:
        for key in act.keys():
            if key == fromName:
                fromAccount = act.get(key)
            if key == toName:
                toAccount = act.get(key)
    if fromAccount == None or toAccount == None:
        print('查無此人')
    else:
        fromAccount.transfer(x, toAccount)

def createAccount():
    accountName = input('請輸入開戶人名稱: ')
    x = int(input('請輸入開戶金額: $'))
    account = act.Account(x)
    dict = {accountName: account}
    list.append(dict)

# 系統選單
while True:
    print('系統選單:')
    print('----------')
    print('1. 查詢')
    print('2. 存款')
    print('3. 提款')
    print('4. 轉帳')
    print('5. 開戶')
    print('6. 解約')
    print('9. 離開')
    print('----------')
    no = int(input('請選擇(1~9): '))
    if no == 1:
        display()
    elif no == 2:
        save()
    elif no == 3:
        withdraw()
    elif no == 4:
        transfer()
    elif no == 5:
        createAccount()
    elif no == 9:
        break
    os.system('pause') # 暫停(按下任意見後繼續...)

print('程式結束')