from tkinter import *
root = Tk()

c = Canvas(root, width=200, height=200, bg='pink')
c.pack()

c.create_text(100, 100, text="Hello World,\nPython\nand Tk",
              justify=CENTER, font="Verdana 14")
c.create_text(200, 200, text="About this",
              anchor=SE, fill="grey")

root.mainloop()