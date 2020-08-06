report = "台積電目前價格每股315元,非常適合買進"
amount = 4000  # 想買 1000 股(一張)
price = report[9:12]
print(price, type(price))
cost = amount * int(price)  # 請算出買進成本
print(cost)
