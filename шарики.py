from tkinter import *
from random import randrange as rnd, choice
import time
import math

root = Tk()
root.geometry('600x600')
canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

colors = ['crimson', 'lightpink', 'orchid','lavender', 'thistle', 'plum', 'violet', 'fuchsia', 'mediumvioletred', 'mediumorchid', 'mediumpurple', 'blueviolet', 'darkviolet',
          'salmon', 'lightcoral', 'darkorchid','darkmagenta','purple', 'indigo', 'hotpink', 'deeppink']
class ball (object):
    '''создать класс шариков
    x,y - координаты центра шарика
    r - радиус шарика
    vx,vy - изменение координат центра шарика
    color - цвет шарика'''
    def __init__(self,canv,x,y,r,vx,vy,color):
        self.canv=canv
        self.x=x
        self.y=y
        self.r=r
        self.vx=vx
        self.vy=vy
        self.color=color

'''создание набора шариков'''
balls = []
for i in range(3):
    balls.append(ball(canv,rnd(100,500),rnd(100,300),rnd(30,50),rnd(20,40),rnd(20,40), choice(colors)))

class square (object):
    def __init__(self, canv, x,y,a,vx,vy,color):
        '''создать класс квадратиков
            x,y -координаты "центра" (точки пересечения диагоналей) квадратика
            a - сторона квадратика
            vx,vy - изменения координат центра квадратика
            color - цвет квадратика'''
        self.canv=canv
        self.x=x
        self.y=y
        self.a=a
        self.vx=vx
        self.vy=vy
        self.color=color

'''создание набора квадратиков'''
squares = []
for i in range(3):
    squares.append(square(canv,rnd(100,500),rnd(100,500),rnd(30,50),rnd(20,40),rnd(20,40), choice(colors)))

def move_figures():
    '''создать функцию, которая будет перемещать шарики'''

    '''смена координат'''
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

        squares[i].y += squares[i].vy
        squares[i].x += squares[i].vx
        if squares[i].x > 600 - squares[i].a:
            squares[i].vx = -squares[i].vx
        if squares[i].x < 0 + squares[i].a:
            squares[i].vx = -squares[i].vx
        if squares[i].y > 400 - squares[i].a:
            squares[i].vy = -squares[i].vy
        if squares[i].y < 0 + squares[i].a:
            squares[i].vy = -squares[i].vy
    '''удаление предыдущих шариков'''
    canv.delete(ALL)
    '''создание новых шариков'''
    for i in range(3):
        canv.create_oval(balls[i].x - balls[i].r, balls[i].y - balls[i].r, balls[i].x + balls[i].r, balls[i].y + balls[i].r, fill=balls[i].color, width=0)
        canv.create_rectangle(squares[i].x - squares[i].a, squares[i].y - squares[i].a, squares[i].x + squares[i].a,
                              squares[i].y + squares[i].a, fill=squares[i].color, width=0)
    root.after(40, move_figures)

'''cоздание табло для циферок'''
l = Label(bg='pink', fg='black', width=50)


a=0
b=0
def counter(event):
    '''cоздание счетчика циферок за попадание по фигурам'''
    for i in range(3):
        '''считаем, есть попадание внутрь шарика или нет'''
        p =math.sqrt ((balls[i].x - event.x) ** 2 + (balls[i].y - event.y) ** 2)
        global a
        global b
        global l
        '''если попадание есть, то начисляем циферки'''
        if balls[i].r>p:
            a = a + 1
            l['text'] = str('POINTS: ')+str(a + b)+'\n'+str('balls: ')+str(a)+'\n'+str('squares: ')+str(int(b/2))+'\n'+str('you are awesome 😘')
        '''считаем, есть попадание внутрь квадратика или нет'''
        q =math.sqrt ((squares[i].x - event.x) ** 2 + (squares[i].y - event.y) ** 2)
        '''если попадание есть, то начисляем циферки (больше, чем за шарик!)'''
        if squares[i].a>q:
            b = b + 2
            l['text']=str('POINTS: ')+ str(a+b)+'\n'+str('balls: ')+str(a)+'\n'+str('squares: ')+str(int(b/2))+'\n'+str('you are awesome 😘')

def click(event):
    '''создать функцию, которая будет по клику изменять циферки на табло'''
    canv.bind('<Button-1>', counter)

'''сделать так, чтобы рисовались фигуры, которые двигаются, а по клику считались циферки за попадание по ним и выводились на табло'''
move_figures()
canv.bind('<Button-1>', click)
l.pack()
mainloop()