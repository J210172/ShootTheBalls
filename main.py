import pygame


def print_hi(name):
    print(f'Hi, {name}')

class Game:
    def __init__(self):
        self.name = "ShootTheBalls"
        self.status = True

    def game_loop(self):
        while self.status:
            pass

if __name__ == '__main__':
    myGame = Game()

