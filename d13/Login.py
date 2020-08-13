users = [
    {'name': 'john', 'password': '4321'},
    {'name': 'admin', 'password': '1234'},
]

def loginCheck(u, p):
    check = None
    for user in users:
        if user['name'] == u and user['password'] == p:
            check = True
        else:
            check = False
    return check

if __name__ == '__main__':
    result = loginCheck('abc', '1111')
    print(result)

