def usd(money):
    return money / 30

def jpy(money):
    return money * 4

def exchange(func, money):
    money -= 100
    return func(money)

if __name__ == '__main__':
    print(exchange(jpy, 500))
    print(exchange(usd, 400))

