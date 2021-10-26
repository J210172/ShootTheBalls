import pygame

class Bullet():
    position: tuple  # position of the bullet
    speed: tuple  # speed vector of the bullet
    nCollisions: int  # for the bullet lifetime

    def __init__(self, position: tuple, speed: tuple, damage: int = 10, size: tuple = (5, 5)):
        self.position = position
        self.speed = speed
        self.damage = damage
        self.size = size
        self.nCollisions = 0

    def __str__(self):
        return f"position: {self.position}, speed: {self.speed} damage: {self.damage}, bullet size: {self.size}, collisonN: {self.nCollisions}"

    def update(self, maxx, maxy):
        x, y = self.position
        sx, sy = self.speed
        px = x + sx
        py = y + sy
        if maxx is not None and maxy is not None:
            if px < 0:
                self.nCollisions += 1
                px = 0
                self.speed = sx * -1, sy
            if px > maxx:
                self.nCollisions += 1
                px = maxx
                self.speed = sx * -1, sy
            if py < 0:
                self.nCollisions += 1
                py = 0
                self.speed = sx, sy * -1
            if py > maxy:
                self.nCollisions += 1
                py = maxy
                self.speed = sx, sy * -1
        self.position = px, py

    def getBullet(self):
        return pygame.Rect(self.position, self.size)