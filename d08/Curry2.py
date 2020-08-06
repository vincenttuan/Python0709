# admin 因為登入成功可以得到指定的 100 元
# hacker 因為登入失敗只可以得到 0 元
def login(username):
    def loginPass(money):
        return 100 if money > 100 else money
    def loginFail(money):
        return 0
    return loginPass if username == 'admin' else loginFail

print(login('admin')(100))
print(login('hacker')(100))