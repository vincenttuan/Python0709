# 自動會將所有分數全部 +10
def add10(scores):
    for i in range(0, len(scores)):
        scores[i] += 10

# 針對單一分數 +10
def add10_singleValue(s):
    global score
    score = s + 10

def add10_singleValue2(s):
    return s + 10

if __name__ == '__main__':
    scores = [50, 60, 70]
    add10(scores)
    print(scores)

    score = 90
    add10_singleValue(score)
    print(score)

    score = 90
    score = add10_singleValue2(score)
    print(score)