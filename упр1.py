import math as m
def sentence(x):
    a=1/m.exp(m.sin(x)+1)
    b=5/4+1/x**15
    c=a/b
    d=1+x**2
    return m.log(c,d)

x1=1
x2=10
x3=1000

y1=sentence(x1)
y2=sentence(x2)
y3=sentence(x3)

print(y1, y2, y3)