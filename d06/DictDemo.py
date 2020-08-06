# 字典資料格式
fruits = {'orange':20, 'apple':10, 'watermelon':30}
# 利用 get(放入key值) 得到 value 值
print('orange 幾元', fruits.get('orange'))
print('apple 幾元', fruits.get('apple'))
print('watermelon 幾元', fruits.get('watermelon'))
print('banana 幾元', fruits.get('banana'))
print(fruits)
# setdefault(Key值, 預設值(若找不到此元素))
print('banana 幾元', fruits.setdefault('banana', 70))
print(fruits)
print('apple 幾元', fruits.setdefault('apple', 100))
print(fruits)
# 取得所有的 key 值
names = fruits.keys()
print(names, type(names))
# 取得所有的 value 值
values = fruits.values()
print(values, type(values), sum(values))
