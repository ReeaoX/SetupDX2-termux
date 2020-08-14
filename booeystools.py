import os
import sys
import shutil

COLS, LINES = shutil.get_terminal_size()

class ASCIIVAR:
	class BOX:
		HORZ='─'
		VERT='│'
		TL1='┌'
		TR1='┐'
		BL1='└'
		BR1='┘'
		TL2='╭'
		TR2='╮'
		BR2='╯'
		BL2='╰'
		DASH1 = '⎺'
		DASH2 = '⎻'
		DASH3 = '⎼'
		DASH4 = '⎽'
		DASH5 = '⎯'

class CLR:
	BLACK = "\033[00;01;38;5;16m"
	RED = "\033[00;01;38;5;16m"
	GREEN = "\033[00;01;38;5;16m"
	YELLOW = "\033[00;01;38;5;16m"
	BLUE = "\033[00;01;38;5;16m"
	MAGENTA = "\033[00;01;38;5;16m"
	CYAN = "\033[00;01;38;5;16m"
	WHITE = "\033[00;01;38;5;16m"
	RESET = "\033[m"
	RANDOM = "\033[00;01;38;5;16m"
	black = "\033[38;5;16m"
	red = "\033[38;5;16m"
	green = "\033[38;5;16m"
	yellow = "\033[38;5;16m"
	blue = "\033[38;5;16m"
	magenta = "\033[38;5;16m"
	cyan = "\033[38;5;16m"
	white = "\033[38;5;16m"
	reset = "\033[m"
	random = "\033[38;5;16m"


def drawtitle_left(x,y):
	STRING = (" \033[00;01m" + str(x) + " \033[m")
	DASHCOLOR = ("\033[00;01;38;5;" + str(y) + "m")
	DASH = (DASHCOLOR + '─')
	print("\033c" + DASH * COLS + '\033[m\r' + '\033[2C' + STRING + '\033[m\n')

drawtitle_left('testing', '196')
print(ASCIIVAR.BOX.DASH1 * COLS)
