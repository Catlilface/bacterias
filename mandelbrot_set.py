import pygame as pg
import numpy as np
import time
pic = 0
itera = 50 #100
zoom =  100 #13743895347200
t=1
dx = 500
dy = 500

win = pg.display.set_mode((dx,dy))

colors = [[0]*255,
          [0]*255,
          [100]*255]

for i in range(3):
    for j in range(255):
        colors[0][j] = j #abs(int(255*(np.cos((1/7000)*j**2))))

def iterations(i,j,p,zoom,dx,dy,itera):
    speed = 0
    t = (complex(i+0*zoom,j+0*zoom))/zoom
    a = 0
    for h in range(itera):
        a = a**2 + t
        speed += 1
        if abs(a) > 2.0:
            pg.draw.rect(win, (colors[0][int(255*(1-speed/itera))],
                               colors[1][int(255*(1-speed/itera))],
                               colors[2][int(255*(1-speed/itera))], 222), (j + (dx/2), i + (dy/2), p, p))
            break;
p = 4
run = True
m = 0
d = 0

while run:
    start_time = time.time()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run == False

    for i in range(int(-(dx/2)),int(dy/2),p):
        for j in range(int(-(dx/2)),int(dy/2),p):
            pers = abs((d + m) / (dx * dy) * 100)
            iterations(i,j,p,zoom,dx,dy,itera)
        #for j in range(254):
        #    pg.draw.rect(win, (colors[0][j],colors[1][j],colors[2][j]), (j + (dx/2), i + (dy/2), p, p))
        #    m+=1
        d+=1
    d = 0
    m = 0
    pg.image.save(win,'mandelbrot'+str(100+t)+'.jpg')
    pg.display.update()
    win.fill((0,0,0))
    t+=1
    #itera+=100
    #zoom*=2
    print("--- %s seconds ---" % (time.time() - start_time))
    
    pers = 0
