import random

while True:
    n = random.randint(1, 100)
    # 若 n 等於 3 的倍數才印出
    if n % 3 == 0:
        print(n)
        continue
    # 若 n 等於 11 的倍數就停止 (break)
    if n % 11 == 0:
        break
