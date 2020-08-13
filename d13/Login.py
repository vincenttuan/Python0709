class LoginException(Exception):
    def __init__(self, message) -> None:
        self.message = message

    def __str__(self) -> str:
        return "登入錯誤原因:" + self.message

users = [
    {'name': 'john', 'password': '4321'},
    {'name': 'admin', 'password': '1234'},
]

def loginCheck(u, p):
    # 先確認是否有找帳號 ?
    check = None
    for user in users:
        if user['name'] == u:
            check = True

    if not check:
        e = LoginException('無此帳號')
        raise e # 將錯誤物件拋出

    # 密碼是否正確 ?
    check = None
    for user in users:
        if user['name'] == u and user['password'] == p:
            check = True

    if not check:
        e = LoginException('密碼錯誤')
        raise e # 將錯誤物件拋出

    return check

if __name__ == '__main__':
    try:
        result = loginCheck('admin', '1234')
    except LoginException as e:
        print(e)
    else:
        print(result)

