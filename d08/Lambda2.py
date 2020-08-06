id = 'A233334444'
sex = id[1]  # 1: 男生, 2:女生
dict = {
        "1": lambda : print('男生'),
        "2": lambda : print('女生')
       }
dict.get("1")()
