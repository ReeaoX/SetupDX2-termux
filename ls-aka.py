#!/usr/bin/env python3

### IMPORTS ###
#
import sys
import os


### VARS ###
#
HOME = os.getenv('HOME')
DX2AKA = os.getenv('DX2ALIASES')
lsdotaka = (DX2AKA + '/ls.aka')
defaultopts = """export LS_OPTS="-C -w \$COLUMNS --color=always --group-directories-first"
"""
dotsfirst = """export LC_COLLATE='C'
"""
defaultaliases = """
alias ls="ls $LS_OPTS"
alias ll="ls -l"
alias la="ls -A"
alias lla="ls -Al"
alias l=ls
"""
DefWithDotsfirst = (dotsfirst + defaultopts + defaultaliases)


### FUNCTIONS ###
#
def askdotsfirst():
	'''
	FUNC:	askdotsfirst()
	DESC:	Used to ask user if they want to enable
			the option to group and list hideen	files
			and dirs before listing normal files and
			dirs
	'''
	print('When listing directory\'s contents, do you want to group and list hidden files (filename preceeded by a dot - ex: .filename) first?')
	askdotsopts = input('[Y/n]: ')
	if askdotsopts == 'Y' or askdotsopts == 'y' or askdotsopts == '':
		print('Grouping hidden files/dirs and displaying them before other files/dirs\n')
	elif askdotsopts == 'N' or askdotsopts == 'n':
		dotsfirst = ''


def editpresetlsoptions():
	'''
	FUNC:	editpresetlsoptions()
	DESC:	Used to edit the preset default ls options, one
			option at a time
	'''
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

def entercustomopts():
	'''
	FUNC:	entercustomopts()
	DESC:	Used to get input from user
	TYPE:	String
	XTRA:	Value to be saved as $LS_OPTS
	'''
	defaultopts = input('Enter the set of options that you want to use as the default options for the ls command\n: ', end='')

def customoptions():
	'''
	FUNC:	customoptions()
	DESC:	Used to ask user if they want to use the
			default preset options, edit the preset
			options, or enter and use a custom value
			of their own.
	'''
	print('The current default options for the ls command is:\n\t' + defaultopts + '\n\n')
	cusopt_opt = input('What would you like to do?\n\t1)Use the current default options\n\t2) Enter a different set of options to use as the default options\n\n: ')
	if cusopt_opt == '1':
		print('Using the default options set for the ls command.\n')
	elif cusopt_opt == '2':
		entercustomopts()

print('\033[00;01m[ \033[38;5;190mWAIT\033[00;01m ] - Generating alias start-up file for ls commands.\r', end='')
if os.path.exists(lsdotaka) == False:
	f = open(lsdotaka, "w")
	f.write(dotsfirst + defaultopts + defaultaliases)
	f.close()
	print('\033[00;01m[ \033[38;5;46mDONE\033[00;01m ] - Generating alias start-up file for ls commands.\n [+] File successfully created.\n')
else:
	print('\033[00;01m[ \033[38;5;46mDONE\033[00;01m ] - Generating alias start-up file for ls commands.\n [+] File already exists!\n')

del HOME, DX2AKA, lsdotaka, dotsfirst, defaultopts, defaultaliases


