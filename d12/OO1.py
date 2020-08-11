class Human:
    name = ''
    age = 0
    sex = ''

    def __str__(self) -> str:
        return self.name + ', ' + str(self.age) + ', ' + self.sex


if __name__ == '__main__':
    h1 = Human()
    h1.name = 'Vincent'
    h1.age = 18
    h1.sex = '男'

    h2 = Human()
    h2.name = 'Anita'
    h2.age = 17
    h2.sex = '女'

    print(h1, h2)

