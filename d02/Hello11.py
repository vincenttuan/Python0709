import math
# 求平面二點間的距離
# a點座標 (10, 2) b點座標 (4, 30)
# 求 ab 的直線距離
x0, y0 = 10, 2
x1, y1 = 4, 30
d = math.sqrt(math.pow(x0-x1, 2) + math.pow(y0-y1, 2))
result = 'a點座標({0}, {1}) b點座標({2}, {3}) 直線距離 {4:.2f}'.format(x0, y0, x1, y1, d)
print(result)