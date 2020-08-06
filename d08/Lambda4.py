if __name__ == '__main__':
    lev = ['E', 'E', 'E', 'E', 'E', 'E', 'D', 'C', 'B', 'A', 'A']
          # 0    1    2    3    4    5    6    7    8    9    10
    dict = {
        'level' : lambda score : print(lev[score//10])
    }
    dict.get('level')(95)  # 得到 A
    dict.get('level')(85)  # 得到 B
    dict.get('level')(75)  # 得到 C
    dict.get('level')(65)  # 得到 D
    dict.get('level')(55)  # 得到 E
    dict.get('level')(25)  # 得到 E