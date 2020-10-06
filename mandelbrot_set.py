import pygame as pg
import numpy as np
pic = 0
itera = 2000 #100
zoom = 100 #13743895347200
t=1
dx = 500
dy = 500
win = pg.display.set_mode((dx,dy))

def iterations(i,j,p,zoom,dx,dy,itera):
    t = (complex(i+0.001643721971153*zoom,j+0.822467633298876*zoom))/zoom
    a = 0
    for h in range(itera):
        a = a**2 + t
        if abs(a) > 10000.0:
            break;
    if abs(a) >= abs(complex(i,j)):
        x = abs(complex(i,j))/(abs(a)+1/900*zoom)
        pg.draw.rect(win, (int(255*np.e**(-abs(a)/h)),
                           int(255*np.e**(-abs(a)/h)),
                           int(255*np.e**(-abs(a)/h))), (j + (dx/2), i + (dy/2), p, p))
p = 2
run = True
m = 0
d = 0
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run == False

    for i in range(int(-(dx/2)),int(dy/2),p):
        for j in range(int(-(dx/2)),int(dy/2),p):
            pers = abs((d + m) / (dx * dy) * 100)
            iterations(i,j,p,zoom,dx,dy,itera)
            m+=1
        d+=1
    d = 0
    m = 0
    pg.image.save(win,'mandelbrot'+str(100+t)+'.jpg')
    pg.display.update()
    win.fill((0,0,0))
    t+=1
    print(zoom)
    #itera+=50
    #zoom*=2
    pers = 0
