import pygame as pg
import numpy as np

pg.init()
win = pg.display.set_mode((900,900))

def liner(dots):
    pg.draw.aalines(win, (255,255,255), True, dots, True)

def gravity(dots,dotss):
    for i in range(len(dots)):
        dotss[i][1] += .1
        dots[i][1] += dotss[i][1]

def collisions(dots, dotss):
    for i in range(len(dots)):
        if dots[i][1] >= 700:
            dotss[i][1] *= -.5
            dots[i][1] = 700
        if dots[i][0] <= 0 or dots[i][0] >= 900:
            dotss[i][0] *= -1


    

dots_vectors = [[0,-10],
                [0,-10],
                [0,-10],
                [0,-10],
                [0,-10],
                [0,-10]]

dots = [[400,400],
        [420,430],
        [450,450],
        [475,425],
        [500,400],
        [450,300]]


run = True
while run:
    win.fill((0,0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run == False
    liner(dots)
    collisions(dots,dots_vectors)
    gravity(dots,dots_vectors)
    
    pg.draw.line(win, (255, 255, 255), (0,700),(900,700))
    pg.display.update()
    pg.time.delay(16)
