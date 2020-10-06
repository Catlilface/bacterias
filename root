import pygame as pg
import numpy as np

win = pg.display.set_mode((900,900))
pg.init()

def motion(bacteria):
    for i in range(len(bacteria)):
        if bacteria[i][3][0] + int(bacteria[i][4][0]*np.cos(bacteria[i][4][1])) <= 10 or bacteria[i][3][0] + int(bacteria[i][4][0]*np.cos(bacteria[i][4][1])) >= 890:
            bacteria[i][4][1] = np.pi - bacteria[i][4][1]
        if bacteria[i][3][1] + int(bacteria[i][4][0]*np.sin(bacteria[i][4][1])) <= 10 or bacteria[i][3][1] + int(bacteria[i][4][0]*np.sin(bacteria[i][4][1])) >= 890:
            bacteria[i][4][1] = -bacteria[i][4][1]
        bacteria[i][3][0] += int(bacteria[i][4][0]*np.cos(bacteria[i][4][1]))
        bacteria[i][3][1] += int(bacteria[i][4][0]*np.sin(bacteria[i][4][1]))
        

def render(bacteria):
    for i in range(len(bacteria)):
        pg.draw.circle(win, (bacteria[i][0], bacteria[i][1], bacteria[i][2]), bacteria[i][3], 10)

p = 180

bac = np.array([[255,0,0,[100,400],[4,1],np.random.random()],
                [0,255,0,[200,600],[7,3],np.random.random()],
                [0,0,255,[200,720],[3,-2],np.random.random()],
                [125,125,125,[450,450],[5,3],np.random.random()],
                [125,0,0,[100,400],[2,1],np.random.random()],
                [0,125,0,[200,600],[3,3],np.random.random()],
                [0,0,125,[200,720],[4,-2],np.random.random()],
                [255,255,255,[450,450],[8,3],np.random.random()]])


run = True
while run:
    win.fill((0,0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run == False
    
    render(bac)
    motion(bac)
    
    #pg.time.delay(100)
    pg.display.update()
