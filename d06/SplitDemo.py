data = '170,60'

list = data.split(",")
print(list, type(list))
print(list[0], type(list[0]))
print(list[1], type(list[1]))
h = float(list[0])
w = float(list[1])
bmi = "%.2f" % (w/(h/100)**2)
print(bmi)