import math
import time
import numpy as np
from tkinter import *
from PIL import Image, ImageTk


# define class
class PaintApp:

	# define class variables #
	drawing_tool = "line"
	left_but = "up"
	width, height = 200, 200
	center = height // 2
	white = (255, 255, 255)
	black = (0, 0, 0)
	red = (255, 0, 0)
	blue = (0, 0, 255)
	green = (0, 128, 0)
	yellow = (255, 255, 0)
	cyan = (0, 255, 255)
	magenta = (255, 0, 255)

	# initialize #
	def __init__(self, root):
		drawing_area = Canvas(root)

		drawing_area.pack()

		drawing_area.bind("<Motion>", self.motion)
		drawing_area.bind("<ButtonPress-1>", self.left_but_down)
		drawing_area.bind("<ButtonRelease-1>", self.left_but_up)
		self.create_widgets()


	x_pos, y_pos = None, None
	x1_line_pt, y1_line_pt, x2_line_pt, y2_line_pt = None, None, None, None

	# catch mouse down #
	def paint(self, event=None):
		x1, y1 = (event.x - 1), (event.y - 1)
		x2, y2 = (event.x + 1), (event.y + 1)
		drawing_area.create_oval()


	def left_but_down(self, event=None):
		self.left_but = "down"
		self.x1_line_pt = event.x
		self.y1_line_pt = event.y

	# catch mouse up #
	def left_but_up(self, event=None):
		self.left_but = "up"

		self.x_pos = None
		self.y_pos = None

		self.x2_line_pt = event.x
		self.y2_line_pt = event.y

		if self.drawing_tool == "line":
			self.line_draw(event)

	# catch mouse move #
	def motion(self, event=None):
		if self.drawing_tool == "pencil":
			self.pencil_draw(event)

	# draw pencil #
	def pencil_draw(self, event=None):
		if self.left_but == "down":
			if self.x_pos is not None and self.y_pos is not None:
				event.widget.create_line(self.x_pos, self.y_pos, event.x, event.y, smooth=TRUE)
			self.x_pos = event.x
			self.y_pos = event.y

	# draw line #
	def line_draw(self, event=None):
		if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
			event.widget.create_line(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt, smooth=True, fill="blue")

	# draw arc #
	def arc_draw(self, event=None):
		if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
			coords = self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt
			event.widget.create_arc(coords, start=0, extent=150, style=ARC)
	# lanczos filtering #

	def lanczos(self, y):
		if y == 0:
			return 1
		if y >= 10 or y < 10 and y is not 0:
			return (10*np.sin(((2*np.pi)/20)*y)*np.sin((((2*np.pi)/20)/10)*y))*(np.pi**2 * y**2)
		else:
			return 0

	# draw text #
	def create_widgets(self):
		self.export = Button(self)
		self.export["text"] = "Export"
		self.export["command"] = self.ex
		self.export.pack(side="top")


root = Tk()
paint_app = PaintApp(root)
root.mainloop()
