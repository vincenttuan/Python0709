data = '170,60&160,48'
# 試算出這二筆 bmi 值各是多少 ?

for row in data.split("&"):
    print(row, type(row))
    h, w = row.split(",")
    bmi = "%.2f" % (float(w)/(float(h)/100)** 2)
    print(bmi)
