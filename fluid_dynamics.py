
import pygame as pg
import numpy as np

pg.init()
win = pg.display.set_mode((900,900))

def thermal(temp):
    for i in range(89):
        for j in range(89):
            temp[i][j] = (temp[i][j+1] + temp[i][j-1] + temp[i+1][j] + temp[i-1][j])/4

class cell:
    def __init__(self, x, y, temp):
        self.x = x
        self.y = y
        self.temp = 255*(np.tanh(.00001*temp))
        pg.draw.rect(win, (self.temp, self.temp, self.temp), (self.x, self.y, 10, 10))

temp = np.array([[0]*90]*90)
temp[45][45] = 10000

print(temp)
t = 0
run = True
while run:
    x = 30
    y = 30
    t += 1
    win.fill((0,0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run == False
    thermal(temp)
    for i in range(0, 900, 10):
        for j in range(0, 900, 10):
            cell(i, j, temp[i//10][j//10])
            #temp[i//10][j//10] /= 1.01
    if t % 9 == 0:
        x = 60
        y = 60
        temp[x][y] = 300
    temp[x][y] = 310
    pg.display.update()
