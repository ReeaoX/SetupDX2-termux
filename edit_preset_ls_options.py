#!/usr/bin/env python3

import os

def editpresetlsoptions():
	lscoled = ('-C ', end='')
	screenswidth = ('-w \$COLUMNS', end='')
	colors = ('--color=always ', end='')
	dirsfirst = ('--group-directories-first ', end='')
	defaultopts = (lscoled + screenswidth + colors + dirsfirst)

	print('Current ls options set to: ' + defaultopts + '\n')
	print('List contents alphabetically in columns?')
	colopts = input('[Y/n]: ')
	if colopts == 'Y' or colopts == 'y' or colopts == '':
		print('Using \'-C\' option (List contents by columns)')
	elif colopts == 'N' or colopts == 'n':
		lscoled = ''
	del colopts

	print('Use the entire screen\'s width (The value of \$COLUMNS)?')
	widthopts = input('[Y/n]: ')
	if widthopts == 'Y' or widthopts == 'y' or widthopts == '':
		print('Using the option \'-w \COLUMNS\' (Use the entire screen\'s width when listing contents, using the value of \$COLUMNS for the screen\'s width size)')
	elif widthopts == 'N' or widthopts == 'n':
		screenswidth = ''
	del widthopts

	print('Enable colors when listing contents?')
	colorsopts = input('[Y/n]: ')
	if coloropts == 'Y' or coloropts == 'y' or coloropts == '':
		print('Enabling the option \'--color=always\' (Enabling colors)')
	elif coloropts == 'N' or coloropts == 'n':
		colors = ''
	del coloropts

	print('Group and list directories prior to other files?')
	dirsopts = input('[Y/n]: ')
	if dirsopts == 'Y' or dirsopts == 'y' or dirsopts == '':
		print('Enabling the option \'--group-directories-first\' (Grouping and listing directories before other files/contents)')
	elif dirsopts == 'N' or dirsopts == 'n':
		dirsfirst = ''
	del dirsopts
	defaultopts = (lscoled + screenswidth + colors + dirsfirst)

	print('New ls options is now:\n\t' + defaultopts + '\n')
