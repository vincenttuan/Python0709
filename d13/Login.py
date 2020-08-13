users = [
    {'name': 'john', 'password': '4321'},
    {'name': 'admin', 'password': '1234'},
]

def loginCheck(u, p):
    check = None
    # 先確認是否有找帳號 ?
    for user in users:
        if user['name'] == u:
            check = True

    if not check:
        e = Exception('無此帳號')
        raise e # 將錯誤物件拋出

    # 密碼是否正確 ?
    check = None
    for user in users:
        if user['name'] == u and user['password'] == p:
            check = True

    if not check:
        e = Exception('密碼錯誤')
        raise e # 將錯誤物件拋出

    return check

if __name__ == '__main__':
    try:
        result = loginCheck('admin', '1234')
    except Exception as e:
        print(e)
    else:
        print(result)

