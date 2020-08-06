def calc(id, no, *score, **info):
    print(type(score), score)
    print(type(info), info)
    print('%d 姓名:%s 座號:%d 總分:%d 學員資料%s' % (
            id, info.get('name'), no, sum(score), info))

if __name__ == '__main__' :
    calc(1, 5, 100, 90, 80, name='Vincent', age=18)

