import pygame


def print_hi(name):
    print(f'Hi, {name}')

class Game:
    def __init__(self, name):
        self.name = name
        self.status = True
        self.setUp()

    def setUp(self):
        thePlayer = s.Player((mx / 2, my / 2), (5, 5), size=(20, 20))
        self.ED = (255, 0, 0)
        self.size = (700, 500)
        self.mx, my = self.size
        self.screen = pygame.display.set_mode(self.size)
        self.carryOn = True
        self.clock = pygame.time.Clock()
        self.bulletsAlive = []

    def makeBullet(self, point):
        x1, y1 = point
        global bulletsAlive
        x0, y0 = thePlayer.position
        vx , vy = x1 - x0, y1 - y0
        m = math.sqrt(vx*vx+vy*vy)
        speed = round(vx/m * 5, 2) , round(vy/m * 5, 2)
        print(speed)
        bulletsAlive.append(s.Bullet(thePlayer.position, speed))

    def game_loop(self):
        while self.status:
            pass

if __name__ == '__main__':
    myGame = Game()

