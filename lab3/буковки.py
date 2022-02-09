from tkinter import *

root = Tk()
e = Entry(width=100)
b = Button(text="Преобразовать буковки")
l = Label(bg='pink', fg='black', width=50)


def strToSortlist(event):
    s = e.get()
    s = s.split()
    s.sort()
    l['text'] = ' '.join(s)

b.bind('<Button-1>', strToSortlist)

e.pack()
b.pack()
l.pack()
root.mainloop()