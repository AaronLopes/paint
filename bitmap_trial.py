import cv2
import numpy as np

drawing = False  # True if mouse is pressed
mode = False  # If True, draw rectangle. Press 'm' to toggle to curve
ix, iy = -1, -1
# RGB colors
white = np.array([255, 255, 255])
black = np.array([0, 0, 0])
red = np.array([255, 0, 0])
blue = np.array([0, 0, 255])
green = np.array([0, 128, 0])
yellow = np.array([255, 255, 0])
cyan = np.array([0, 255, 255])
magenta = np.array([255, 0, 255])

colors = np.array([white, black, red, blue, green, yellow, cyan, magenta])


def translate(arr):
	for r in range(len(arr)):
		for c in range(len(arr[r])):
			color = arr[r][c]
			if np.array_equal(color, white):
				pass
			else:
				arr[r][wave_filter(c)] = color


# wave filter
def wave_filter(y):
	return int(10 * np.sin(((2*np.pi)/40) * y))


# mouse callback function
def draw_circle(event, x, y, flags, param):
	global ix, iy, drawing, mode
	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		ix, iy = x, y
	elif event == cv2.EVENT_MOUSEMOVE and drawing:
		cv2.circle(img, (x, y), 10, (0, 0, 255), -1)
	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False
		cv2.circle(img, (x, y), 10, (0, 0, 255), -1)


# create a black image, a window, and bind the function to window
img = np.full((500, 400, 3), 255, dtype=np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while 1:
	cv2.imshow('image', img)
	k = cv2.waitKey(1) & 0xFF
	if k == ord('m'):
		mode = not mode
	if mode:
		translate(img)
	elif k == 27:
		break
cv2.destroyAllWindows()
