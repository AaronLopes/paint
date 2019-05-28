import numpy as np
from PIL import ImageTk, Image, ImageDraw
from tkinter import *

width = 1600
height = 1200
center = height // 1600

def paint(event, color):
	x1, y1 = (event.x - 1), (event.y - 1)
	x2, y2 = (event.x + 1), (event.y + 1)
	canvas.create_oval(x1, y1, x2, y2, fill=color, width=10)



root = Tk()

# Create Tkinter Canvas
canvas = Canvas(root, width=width, height=height, bg='white')
canvas.pack()

root.mainloop()

