from time import sleep

current_floor = 1

print('有一棟 7 層大樓的電梯系統, 運作如下:')
while True:
    target_floor = input('您現在在 ' + str(current_floor) + ' 樓。請問要去哪一樓？\n>>')
    try:
        target_floor = int(target_floor)
    except ValueError:
        print('格式錯誤，請輸入數字\n')
        continue

    if not(1 <= target_floor <= 7):
        print('請輸入介於 1-7 的整數\n')
        continue

    if target_floor == current_floor:
        continue

    elif target_floor < current_floor:
        print('電梯下樓')
        while target_floor < current_floor:
            print(current_floor)
            current_floor = current_floor - 1
            sleep(1)
        print(current_floor)

    else:
        print('電梯上樓')
        while target_floor > current_floor:
            print(current_floor)
            current_floor = current_floor + 1
            sleep(1)
        print(current_floor)