class Bird:
    def move(self):
        print('我會飛')

class Penguin(Bird):
    def move(self):
        print('我不會飛, 我會走和游泳')


if __name__ == '__main__':
    bird = Bird()
    bird.move()

    penguin = Penguin()
    penguin.move()