class Foo:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def __str__(self) -> str:
        return "x: %d y: %d" % (self.x, self.y)

class Bar:
    def __call__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self) -> str:
        return "x: %d y: %d" % (self.x, self.y)

if __name__ == '__main__':
    foo = Foo(10, 20) # __init__
    print(foo)
    bar = Bar()  # __init__
    bar(10, 20)  # __call__
    print(bar)