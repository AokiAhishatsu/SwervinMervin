# Swervin' Mervin
# (c) Andrew Buntine
# https://github.com/buntine/SwervinMervin

import pygame
import game as g
import settings as s

import os

# Fix FileNotFoundError: [Errno 2] No such file or directory: 'dat/highscores'
os.chdir(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)))

pygame.init()

pygame.display.set_caption("Swervin' Mervin")

if s.FULLSCREEN:
    w_flag = pygame.FULLSCREEN
    pygame.mouse.set_visible(False)
else:
    w_flag = 0

fps_clock = pygame.time.Clock()
window    = pygame.display.set_mode(s.DIMENSIONS, w_flag)
game      = g.Game(window, fps_clock)

while True:
   if game.waiting:
       game.wait()
   else:
       game.play()
