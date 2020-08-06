class Account:
    money = 10000  # 物件屬性/變數/資產

    def save(self, x):
        print("存款: $" + str(x))
        if x <= 0:
            print('提款金額必須 > 0')
            return
        self.money = self.money + x

    def withdraw(self, x):  # x 表示要提款的金額
        print("提款: $" + str(x))
        if x <= 0:
            print('提款金額必須 > 0')
            return
        if x > self.money:
            print('提款金額過大, 餘額不足')
            return
        self.money = self.money - x

    def __str__(self) -> str:
        return "帳戶餘額: $" + str(self.money)


if __name__ == '__main__':
    account1 = Account()  # 建立一個物件
    print(account1)
    account1.withdraw(6000)
    print(account1)
    account1.withdraw(-6000)
    print(account1)
    account1.save(5000)
    print(account1)



