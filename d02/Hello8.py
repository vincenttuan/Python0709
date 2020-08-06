pen = 30
amount = 400
total = pen * amount
print(pen, amount, total)
print(pen, amount, total, sep="&")
print(pen, amount, total, sep=",")
#print('鉛筆每枝15元200枝總共是3000元')
print('鉛筆每枝' + str(pen) + '元' + str(amount) + '枝總共是' + str(total) + '元')
print('鉛筆每枝%d元%d枝總共是%d元' % (pen, amount, total))