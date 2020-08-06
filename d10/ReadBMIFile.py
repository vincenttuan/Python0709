file = open('bmi.csv', 'r')
data = file.read()
print(type(data), data)

file = open('bmi.csv', 'r')
data = file.readlines()
print(type(data), data)