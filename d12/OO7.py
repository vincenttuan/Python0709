class Engine:
    def __init__(self, power) -> None:
        self.power = power

    def __str__(self) -> str:
        return 'engine power: %d ' % (self.power)


class Tires:
    def __init__(self, count) -> None:
        self.count = count

    def __str__(self) -> str:
        return 'tires count: %d ' % (self.count)

class Car(Engine, Tires):
    def __init__(self, power, count, name) -> None:
        Engine.__init__(self, power)
        Tires.__init__(self, count)
        self.name = name;

    def __str__(self) -> str:
        return Engine.__str__(self) + Tires.__str__(self) + 'name: %s' % (self.name)


if __name__ == '__main__':
    car = Car(5000, 4, 'BMW')
    print(car)
