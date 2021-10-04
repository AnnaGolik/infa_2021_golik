from graph import *
import math as m

# sky
penColor(175, 238, 238)
brushColor(175, 238, 238)
rectangle(0, 0, 500, 150)

# ground
penColor(26, 148, 49)
brushColor(26, 148, 49)
rectangle(0, 150, 500, 300)

# house
penColor("black")
brushColor(127, 63, 10)
rectangle(90, 130, 210, 210)

penColor("black")
brushColor("red")
polygon([(152, 80), (210, 130),
         (90, 130), (152, 80)])

penColor("orange")
brushColor(0, 150, 141)
rectangle(130, 155, 170, 185)

# tree
penColor("black")
brushColor("black")
rectangle(400, 140, 410, 200)

penColor("black")
brushColor(26, 102, 46)
circle(405, 85, 20)
moveTo(385, 105)
circle(385, 105, 20)
moveTo(425, 105)
circle(425, 105, 20)
moveTo(405, 115)
circle(405, 115, 20)
moveTo(390, 125)
circle(390, 125, 20)
moveTo(420, 125)
circle(420, 125, 20)

# cloud
brushColor("white")
x = 280
for i in range(2):
    circle(x, 40, 20)
    x += 25
x = 255
for i in range(4):
    circle(x, 60, 20)
    x += 25

# sun
penColor("black")
brushColor("pink")
x = 400
y = 40
moveTo(x, y)
D = list()
for i in range(20):
    x1 = x + 20 * m.sin(2 * i * 0.314)
    y1 = y + 20 * m.cos(2 * i * 0.314)
    D.append((x1, y1))
    x2 = x + 16 * m.sin((2 * i + 1) * 0.314)
    y2 = y + 16 * m.cos((2 * i + 1) * 0.314)
    D.append((x2, y2))

polygon(D)

run()