def calc(x, y):
    # 請自行實作
    a = 2 * x;
    b = y - a;
    rabbit = b / 2;
    return x-rabbit, rabbit

chicken, rabbit = calc(83, 240)
print("雞:%d 兔:%d 隻數:%d 腳數:%d" %
      (chicken, rabbit, chicken+rabbit, (chicken*2+rabbit*4)))
