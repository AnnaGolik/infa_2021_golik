from graph import *
import math as math

# sky
penColor(175, 238, 238)
brushColor(175, 238, 238)
rectangle(0, 0, 500, 150)

# ground
penColor(26, 148, 49)
brushColor(26, 148, 49)
rectangle(0, 150, 500, 300)

def house(x0,y0,m):
    penColor("black")
    brushColor(127, 63, 10)
    rectangle(m*(x0+90), m*(y0+130), m*(x0+210), m*(y0+210))

    penColor("black")
    brushColor("red")
    polygon([(m*(x0+152), m*(y0+80)), (m*(x0+210), m*(y0+130)),
             (m*(x0+90), m*(y0+130)), (m*(x0+152), m*(y0+80))])

    penColor("orange")
    brushColor(0, 150, 141)
    rectangle(m*(x0+130), m*(y0+155), m*(x0+170), m*(y0+185))


house(-50,30,1)
house(400,130,0.6)

def tree(x0,y0,m):
    penColor("black")
    brushColor("black")
    rectangle(m*(x0+400), m*(y0+140), m*(x0+410), m*(y0+200))

    penColor("black")
    brushColor(26, 102, 46)
    circle(m*(x0+405), m*(y0+85), m*20)
    moveTo(m*(x0+385), m*(y0+105))
    circle(m*(x0+385), m*(y0+105), m*20)
    moveTo(m*(x0+425), m*(y0+105))
    circle(m*(x0+425), m*(y0+105), m*20)
    moveTo(m*(x0+405), m*(y0+115))
    circle(m*(x0+405), m*(y0+115), m*20)
    moveTo(m*(x0+390), m*(y0+125))
    circle(m*(x0+390), m*(y0+125), m*20)
    moveTo(m*(x0+420), m*(y0+125))
    circle(m*(x0+420), m*(y0+125), m*20)

tree(200,95,0.7)
tree(-200,25,1)

def cloud(x0,y0,m):
    brushColor("white")
    x = m*(x0+255)
    for i in range(4):
        circle(m*(x+x0), m*(y0+55), m*20)
        x = x+25*m*1.3
    x = m * (x0 + 320)
    for i in range(2):
        circle(m * (x0+x), m * (y0 + 40), m * 20)
        x = x - 25 * m * 1.5

cloud(170,50,0.6)
cloud(-30,15,0.75)
cloud(170,20,0.8)

def sun(x0,y0,m):
    penColor("black")
    brushColor("pink")
    x = 400+x0
    y = 40+y0
    moveTo(x, y)
    D = list()
    for i in range(40):
        x1 = x + m*(20 * math.sin(2 * i * 0.1570))
        y1 = y + m*(20 * math.cos(2 * i * 0.1570))
        D.append((x1, y1))
        x2 = x + m*(18 * math.sin((2 * i + 1) * 0.1570))
        y2 = y + m*(18 * math.cos((2 * i + 1) * 0.1570))
        D.append((x2, y2))

    polygon(D)

sun(-370,-10,1.1)


run()