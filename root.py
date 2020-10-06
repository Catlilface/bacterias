import pygame as pg
import numpy as np

win = pg.display.set_mode((900,900))
pg.init()

def sex(bac1, bac2):
    if (abs(bac1[3][0] - bac2[3][0]) + bac1[4][0]*np.cos(bac1[4][1]) < 20) and (abs(bac1[3][1] - bac2[3][1]) + bac1[4][0]*np.sin(bac1[4][1]) < 20):
        diver = np.random.randint(1,3)
        bac1[0] = int((bac1[0] + bac2[0])/2)
        bac1[1] = int((bac1[1] + bac2[1])/2)
        bac1[2] = int((bac1[2] + bac2[2])/2)

    return bac1

def motion(bacteria): 
    for i in range(len(bacteria)):
        if bacteria[i][3][0] + int(bacteria[i][4][0]*np.cos(bacteria[i][4][1])) <= 10 or bacteria[i][3][0] + int(bacteria[i][4][0]*np.cos(bacteria[i][4][1])) >= 890:
            bacteria[i][4][1] = np.pi - bacteria[i][4][1]
        if bacteria[i][3][1] + int(bacteria[i][4][0]*np.sin(bacteria[i][4][1])) <= 10 or bacteria[i][3][1] + int(bacteria[i][4][0]*np.sin(bacteria[i][4][1])) >= 890:
            bacteria[i][4][1] = -bacteria[i][4][1]
        bacteria[i][3][0] += int(bacteria[i][4][0]*np.cos(bacteria[i][4][1]))
        bacteria[i][3][1] += int(bacteria[i][4][0]*np.sin(bacteria[i][4][1]))
        pg.draw.circle(win, (bacteria[i][0], bacteria[i][1], bacteria[i][2]), bacteria[i][3], 10)

bac = np.array([[255,0,0,[200,450],[4,1],np.random.random()],
                [0,255,0,[500,450],[2,8.6],np.random.random()],
                [0,0,255,[200,40],[6,10],np.random.random()],
                [0,255,255,[100,500],[4,15],np.random.random()],
                [255,255,0,[340,450],[4,12],np.random.random()],
                [255,0,0,[39,450],[2,8.634],np.random.random()],
                [60,60,125,[210,40],[6,102],np.random.random()],
                [0,0,0,[90,500],[4,1512],np.random.random()]])
t = 0
p = -1
run = True
while run:
    win.fill((255,255,255))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run == False
    
    motion(bac)
    
    for i in range(len(bac)):
        for j in range(len(bac)):
            if i != j:
                bac[i] = sex(bac[i], bac[j])

    if np.random.randint(0,1000) == 69:
        bac[np.random.randint(0,8)][np.random.randint(0,3)] = 255
    
   # pg.time.delay(100)
    pg.display.update()
