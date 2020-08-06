exchange = {
    'usd' : lambda money : print(money / 30),
    'jpy' : lambda money : print(money * 4),
}

exchange.get('usd')(900)
exchange.get('jpy')(900)
