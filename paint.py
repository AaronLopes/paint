import cv2
import numpy as np
from datetime import datetime, timedelta

drawing = False  # True if mouse is pressed
mode = False  # If True, draw rectangle. Press 'm' to toggle to curve
ix, iy = -1, -1
# RGB colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 128, 0)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)

colors = [black, white, red, green, blue, yellow, cyan, magenta]
labels = ["black", "white", "red", "green", "blue", "yellow", "cyan", "magenta"]
c_i = 0


# 1d interpolation, a = 2 (filter size), y = x0

"""def interpolate(im):
	lanczos_img = cv2.resize(im, dsize=(1600, 1200), fx=4, fy=4, interpolation=cv2.INTER_LANCZOS4)
	return lanczos_img
"""


def lanczos(y):
	return int(10 * np.sin(((2*np.pi)/40)*y))


def interpolate(im):
	for r in range(len(im)):
		for c in range(len(im[r])):
			color = im[r][c]
			if np.array_equal(color, np.array([255, 255, 255])):
				pass
			else:
				im[r][c + lanczos(c)] = color


# mouse callback function
def draw_circle(event, x, y, flags, param):
	global ix, iy, drawing, mode, colors, c_i
	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		ix, iy = x, y
	elif event == cv2.EVENT_MOUSEMOVE and drawing:
		cv2.circle(img, (x, y), 10, colors[c_i], -1)
	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False
		cv2.circle(img, (x, y), 10, colors[c_i], -1)


# create a black image, a window, and bind the function to window
img = np.full((1600, 1200, 3), 255, dtype=np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while 1:
	cv2.imshow('image', img)
	k = cv2.waitKey(1) & 0xFF
	if k == ord('m'):
		interpolate(img)
	elif k == ord('c'):
		c_i = (c_i + 1) % 8
	elif k == 27:
		break
cv2.destroyAllWindows()
