from tkinter import *
import random

root = Tk()

def run():
    a = random.randint(1,300)
    b = random.randint(1,300)
    print(a,b)
    x0 = a
    y0 = a + 10
    x1 = b
    y1 = b + 10
    canvas.create_rectangle(x0, y0, x1, y1, fill='red')

frame = Frame(root, bg="black")
  
canvas = Canvas(frame,height=300, width=300)
start = Button(text = "Start",command = run)

canvas.pack(padx=1, pady=1)

frame.grid(row = 0,column = 0)
start.grid(row = 1,column = 0)

root.mainloop()