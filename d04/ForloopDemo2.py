# 計算總分的方法
def getSum(scores):
    sum = 0
    for i in range(0, len(scores)):
        sum += scores[i]  # 累加
    return sum

# 計算平均的方法
def getAvg(scores):
    sum = getSum(scores)
    avg = sum / len(scores)
    return avg

# 主程式
scores = [100, 93, 87, 75, 62, 54]  # 數組
print(len(scores))  # 數組的元素個數
# 各科列印
for i in range(0, len(scores)):
    print(scores[i])

# 求總分 ?
sum = getSum(scores)
print("總分: %d" % sum)

# 求平均 ?
avg = getAvg(scores)
print("平均: %.1f" % avg)

