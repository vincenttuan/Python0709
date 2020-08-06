class Account:
    money = 10000  # 物件屬性/變數/資產
    def __str__(self) -> str:
        return "帳戶餘額:" + str(self.money)

if __name__ == '__main__':
    account1 = Account()  # 建立一個物件
    print(account1)



