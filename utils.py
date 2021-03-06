"""Small helper functions, mostly for tkinter"""
import tkinter as tk
import colorsys


def set_col(widg, col):
	"""
	Recursively set color to widget and all of its children

	Args:
		widg (tkinter.Widget): widget to start from
		col (str): color to set, hex or a color name string

	Returns:
		None
	"""

	if not isinstance(widg, tk.Widget):
		return

	widg['bg'] = col
	for child in widg.winfo_children():
		set_col(child, col)


def rgb_to_hex(rgb):
	"""
		translates an rgb tuple of int to a tkinter friendly color code
	"""
	return f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}'


def shift_hue(rgb, delta):
	"""
		shift hue by delta degrees, for a given rgb int tuple
	"""
	angle = delta / 360
	rgbf = tuple(val / 255 for val in rgb)
	h, s, v = colorsys.rgb_to_hsv(*rgbf)
	h += angle
	if h > 1:
		h -= 1
	elif h < 0:
		h += 1

	rgbnew = colorsys.hsv_to_rgb(h, s, v)
	return tuple(round(val * 255) for val in rgbnew)


def scale_brightness(rgb, scale):
	"""
		scale brightness for a given rgb int tuple
	"""
	return tuple(round(val * scale) for val in rgb)


def grid_weight_configure(widg, row_val=1, col_val=1):
	"""
	Set default weights to all rows and columns for a grid layout

	Args:
		widg (tkinter.Widget): widget with a grid layout
		row_val (int or list(int)): default values for rows
		col_val (int or list(int)): default values for columns

	Returns:
		None
	"""
	if not isinstance(widg, tk.Widget):
		return

	for i in range(widg.size()[0]):
		if isinstance(col_val, list):
			widg.columnconfigure(i, weight=col_val[i])
		else:
			widg.columnconfigure(i, weight=col_val)

	for i in range(widg.size()[1]):
		if isinstance(row_val, list):
			widg.rowconfigure(i, weight=row_val[i])
		else:
			widg.rowconfigure(i, weight=row_val)
