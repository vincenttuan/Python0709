# 字串格式化
color = '紅色'
name = '蘋果'
#fruit = color + '的' + name
fruit = '{0}的{1}'.format(color, name)
print(fruit)