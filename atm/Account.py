class Account:
    __money = 0

    def __init__(self, x) -> None:
        self.__money = x

    def save(self, x):
        self.__money -= x

    def __str__(self) -> str:
        return "帳戶餘額: $" + str(self.__money)

