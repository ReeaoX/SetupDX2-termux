#!/usr/bin/env python3

# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2019 Booey <booey@UbuntuMatePi3B>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import shutil

COLS, LINES = shutil.get_terminal_size()

def titlebar(x, y, z):
	TITLE = x
	BG = y
	FG = z
#	print("\033c")
	print('\033c\033[00;01;48;5;' + str(BG) + 'm' + '\033[38;5;' + str(FG) + 'm' + ' ' * COLS + '\r ' + str(TITLE) + '\033[m\n\n')
	del TITLE, BG, FG



def mainmenu():
#	print("\033c")		# clears screen
	titlebar('test', '196', '15')

	
mainmenu()
