import math

import pygame

from Bullet import Bullet
from Player import Player


class Game:
    def __init__(self, name: str = "MyGame"):
        self.name = name
        self.game_status = True
        self.ED = (255, 0, 0)
        self.size = (700, 500)
        self.maxx, self.maxy = self.size
        self.screen = pygame.display.set_mode(self.size)
        self.carryOn = True
        self.clock = pygame.time.Clock()
        self.bulletsAlive = []
        self.thePlayer = Player((self.maxx / 2, self.maxy / 2), (5, 5), size=(20, 20))
        self.setUp()

    def make_bullet(self, point) -> Bullet:
        x1, y1 = point
        x0, y0 = self.thePlayer.position
        vx, vy = x1 - x0, y1 - y0
        m = math.sqrt(vx * vx + vy * vy)
        speed = round(vx / m * 5, 2), round(vy / m * 5, 2)
        print(speed)
        self.bulletsAlive.append(Bullet(self.thePlayer.position, speed))

    def setUp(self):
        self.game_loop()

    def game_loop(self):
        while self.game_status:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_status = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.make_bullet(pygame.mouse.get_pos())

            self.screen.fill((0, 0, 0))

            self.thePlayer.update(self.maxx, self.maxy)
            pygame.draw.rect(self.screen, (255, 0, 0), self.thePlayer.getPlayer())

            for b in self.bulletsAlive:
                if b.nCollisions >= 5:
                    self.bulletsAlive.remove(b)
                else:
                    b.update(self.maxx, self.maxy)
                    pygame.draw.rect(self.screen, (100, 255, 0, 0), b.getBullet())

            pygame.display.flip()
            self.clock.tick(60)
