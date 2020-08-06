import statistics
import random

scores = []
for i in range(0, 10):
    scores.append(random.randint(0, 10))

# 排序
scores.sort()
print(scores)

# 移除最小的2個元素
# __delitem__(0) 移除指定位置的元素
# remove(0) 移除元素是0的資料
scores.__delitem__(0)
scores.__delitem__(0)
print(scores)

# 移除最大的2個元素
scores.__delitem__(len(scores)-1)
scores.__delitem__(len(scores)-1)
print(scores)

mean = statistics.mean(scores)
print("平均:", mean)

stdev = statistics.stdev(scores)
print("標準差:", stdev)

cv = stdev / mean
print('變異係數:', cv)