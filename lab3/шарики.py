from tkinter import *
from random import randrange as rnd, choice
import time
import math

root = Tk()
root.geometry('600x400')
canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue']

class ball (object):
    def __init__(self,canv,x,y,r,vx,vy,color):
        self.canv=canv
        self.x=x
        self.y=y
        self.r=r
        self.vx=vx
        self.vy=vy
        self.color=color

def move_ball():
    for i in range(3):
        balls[i].y += balls[i].vy
        balls[i].x += balls[i].vx
        if balls[i].x > 600 - balls[i].r:
            balls[i].vx = -balls[i].vx
        if balls[i].x < 0 + balls[i].r:
            balls[i].vx = -balls[i].vx
        if balls[i].y > 400 - balls[i].r:
            balls[i].vy = -balls[i].vy
        if balls[i].y < 0 + balls[i].r:
            balls[i].vy = -balls[i].vy
    canv.delete(ALL)
    for i in range(3):
        canv.create_oval(balls[i].x - balls[i].r, balls[i].y - balls[i].r, balls[i].x + balls[i].r, balls[i].y + balls[i].r, fill=balls[i].color, width=0)
    root.after(200, move_ball)

balls = []
for i in range(3):
    balls.append(ball(canv,rnd(100,500),rnd(100,300),rnd(30,50),rnd(20,40),rnd(20,40), choice(colors)))

def draw_move():
    global ball1
    canv.delete(ALL)
    for i in range(3):
        canv.create_oval(balls[i].x - balls[i].r, balls[i].y - balls[i].r, balls[i].x + balls[i].r, balls[i].y + balls[i].r,fill=balls[i].color, width=0)
    root.after(1000, move_ball)

l = Label(bg='pink', fg='black', width=50)

a=0
def counter(event):
    for i in range(3):
        p =math.sqrt ((balls[i].x - event.x) ** 2 + (balls[i].y - event.y) ** 2)
        global a
        global l
        if balls[i].r>p:
            a = a + 1
            l['text']=str('POINTS:'), str(a)

def click(event):
    canv.bind('<Button-1>', counter)

draw_move()
canv.bind('<Button-1>', click)
l.pack()
mainloop()