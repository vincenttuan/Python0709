def calc(x):
    def add(y):
        return x + y
    return add

if __name__ == '__main__':
    ten = calc(10) # x=10 得到 add 函式, 但是還沒呼叫 add
    fif = calc(50) # x=50 得到 add 函式, 但是還沒呼叫 add

    print(ten(20)) # y = 20, 呼叫 add 函式
    print(fif(20)) # y = 20, 呼叫 add 函式
