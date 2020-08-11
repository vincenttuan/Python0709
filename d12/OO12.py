class USD:
    def __get__(self, instance, owner):
        money = instance.money
        return money / 30.5

class JPY:
    def __get__(self, instance, owner):
        money = instance.money
        return money / 0.28

class Exchange:
    usd = USD()
    jpy = JPY()
    def __init__(self, money) -> None:
        self.money = money

if __name__ == '__main__':
    ex = Exchange(10000)
    print(ex.usd)
    print(ex.jpy)

