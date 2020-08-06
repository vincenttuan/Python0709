# 攝氏轉華式
def ctof(value) -> float:
    return value * 9/5 + 32

# 華式轉攝氏
def ftoc(value) -> float:
    return (value-32) * 5/9

if __name__ == '__main__':
    print(ctof(0), ftoc(32))
    print(ctof(24), ftoc(50))