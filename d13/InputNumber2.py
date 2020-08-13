def inputNumber():
    try:
        x = int(input('請輸入分子:'))
        y = int(input('請輸入分母:'))
        z = x / y
        print(x, '/', y, '=', z)
    except ValueError as e:
        print('錯誤類型:', e.__class__.__name__)
        print('您輸入的不是數字, 請重新輸入')
        inputNumber()
    except ZeroDivisionError as e:
        print('錯誤類型:', e.__class__.__name__)
        print('分母不可 = 0, 程式結束...')
        return
    except Exception as e:
        print('錯誤類型:', e.__class__.__name__)
        print('其他錯誤, 程式結束...')
        return

if __name__ == '__main__':
    inputNumber()