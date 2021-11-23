import random
from random import Random

import pygame
import Bolas
from pygame import *
import math

init()

RED = (255, 0, 0)

size = (700, 500)
mx, my = size
screen = display.set_mode(size)
display.set_caption("A simple test")
carryOn = True
clock = time.Clock()
rnd = random.Random()
img = [
    image.load("Bolas\\Bola1 (1).png"),
    image.load("Bolas\\Bola1 (2).png"),
    image.load("Bolas\\Bola1 (3).png"),
    image.load("Bolas\\Bola1 (4).png"),
    image.load("Bolas\\Bola1 (5).png"),
    image.load("Bolas\\Bola1 (6).png"),
    image.load("Bolas\\Bola1 (7).png"),
    image.load("Bolas\\Bola1 (9).png"),
    image.load("Bolas\\Bola1 (10).png"),
    image.load("Bolas\\Bola1 (11).png"),
]
bullets = sprite.Group()

while carryOn:
    for event in pygame.event.get():
        if event.type == QUIT:
            carryOn = False

    if key.get_pressed()[pygame.K_l]:
        bullet = sprite.Sprite()
        bullet.image = img[rnd.randint(0,len(img)-1)]
        bullet.rect = (rnd.randint(0,mx), rnd.randint(0,mx))
        bullets.add(bullet)

    bullets.update(rect=rect.y-5)

    screen.fill((255,255,255))
    bullets.draw(screen)

    display.flip()
    clock.tick(60)