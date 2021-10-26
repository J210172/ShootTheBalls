import pygame

class Player:
    position: tuple  # position of the bullet
    speed: tuple  # speed vector of the bullet

    def __init__(self, position: tuple, speed: tuple, size: tuple = (5, 5)):
        self.position = position
        self.speed = speed
        self.size = size

    def __str__(self):
        return f"position: {self.position}, speed: {self.speed} damage: {self.damage}, bullet size: {self.size}, collisonN: {self.nCollisions}"

    def update(self, mx, my):
        x, y = self.position
        sx, sy = self.speed
        px = x + sx
        py = y + sy

        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            y -= sy
        if key[pygame.K_s]:
            y += sy
        if key[pygame.K_a]:
            x -= sx
        if key[pygame.K_d]:
            x += sx

        """
        if mx is not None and my is not None:
            if px < 0:
                px = 0
                self.speed = sx*-1, sy
            if px > mx:
                px = mx
                self.speed = sx*-1, sy
            if py < 0:
                py = 0
                self.speed = sx, sy*-1
            if py > my:
                py = my
                self.speed = sx, sy*-1
        """
        self.position = x, y

    def getPlayer(self):
        return pygame.Rect(self.position, self.size)