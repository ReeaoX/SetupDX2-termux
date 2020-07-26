#!/usr/bin/env python3

import os
import re
import shutil

__VERSION__ = '4.2'
COLS, LINES = shutil.get_terminal_size()
HOME = os.getenv('HOME')
installyn = None
WAIT = " \033[00;01;38;5;190m[\033[38;5;15mWAIT\033[38;5;190m]\033[m "
PASS = " \033[00;01;38;5;46m[\033[38;5;15mPASS\033[38;5;46m]\033[m "
FAIL = " \033[00;01;38;5;196m[\033[38;5;15mFAIL\033[38;5;196m]\033[m "
DONE = " \033[00;01;38;5;46m[\033[38;5;15mDONE\033[38;5;46m]\033[m "

## DX2 VARS
DX2 = (HOME + '/.DX2')
DX2BIN = (DX2 + '/bin')
DX2RC = (DX2 + '/rc')
DX2DATA = (DX2 + '/data')
DX2FUNCS = (DX2 + '/functions')
DX2BAK = (DX2 + '/backups')
DX2TMP = (DX2 + '/temp')
DX2GIT = (DX2 + '/git')
DX2AKA = (DX2 + '/aliases')
DX2SHORTCUTS = (DX2 + '/.Shortcuts')


def titlebar(x):
	UNDERLINE = '\033[00;01;38;5;196m⎯\033[m'
	TITLE = str(x)
	print('\033[1H' + UNDERLINE * COLS + '\033[m\r' + '\033[3C' + ' \033[00;01m' + TITLE + ' \033[m\n')

def options(x, y, z):
	OPTNUM = str(x)
	OPTSTRING = str(y)
	OPTCOLOR = str(z)
	CLROPT = ('\033[00;01;38;5;' + OPTCOLOR + 'm[\033[38;5;15m' + OPTNUM + '\033[38;5;' + OPTCOLOR + 'm]\033[m')
	print('\t\t' + CLROPT + '\t' + OPTSTRING)

class install:
	def installaddons(x, y, z):
		"""
		syntax: installaddons(addons.bin.colormap, DX2BIN, '/colormap'))
		"""
		FILE = x
		DIR = y
		FILENAME = z
		PATH = (DIR + '/' + FILENAME)
		f = open(PATH, 'w')
		f.write(FILE)
		f.close()
	def chmodbinfiles():
		files = os.listdir(DX2BIN)
		init = 0
		for x in files:
			init = init + 1
			print('\t' + WAIT + str(DX2BIN) + '/' + str(x), end='')
			os.chmod((DX2BIN + '/' + x), 0o766)
			print('\r\t' + DONE)
		print('\033[' + str(init + 1) + 'A\r' + DONE + '\033[' + str(init) + 'B')
	def automatic():
		"""
			FIRST SUB
		"""
		init = 0
		print('\n' + WAIT + '\033[38;5;51mWriting all executable scripts \033[38;5;15m...')
		init = init + 1
		print('\t' + WAIT + 'Writing colormap\'s script ...', end='')
		install.installaddons(addons.bin.colormap, DX2BIN, 'colormap')
		print('\r\t' + DONE)
		init = init + 1
		print('\t' + WAIT + 'Writing webserver\'s script ...', end='')
		install.installaddons(addons.bin.webserver, DX2BIN, 'webserver')
		print('\r\t' + DONE)
		print('\033[' + str(init + 1) + 'A\r' + DONE + '\033[' + str(init) + 'B')
		"""
			SECOND SUB
		"""
		init = 0
		print('\n' + WAIT + '\033[38;5;51mWriting all alias files \033[38;5;15m...')
		init = init + 1
		print('\t' + WAIT + 'Writing ls\'s alias file ...', end='')
		install.installaddons(addons.aliases.ls, DX2AKA, 'ls.aka')
		print('\r\t' + DONE)
		init = init + 1
		print('\t' + WAIT + 'Writing misc alias file ...', end='')
		install.installaddons(addons.aliases.ls, DX2AKA, 'misc.aka')
		print('\r\t' + DONE)
		init = init + 1
		print('\t' + WAIT + 'Writing git\'s alias file ...', end='')
		install.installaddons(addons.aliases.git, DX2AKA, 'git.aka')
		print('\r\t' + DONE)
		init = init + 1
		print('\t' + WAIT + 'Writing colormap\'s alias file ...', end='')
		install.installaddons(addons.aliases.colormap, DX2AKA, 'colormap.aka')
		print('\r\t' + DONE)
		print('\033[' + str(init + 1) + 'A\r' + DONE + '\033[' + str(init) + 'B')
		"""
			THIRD SUB
		"""
		init = 0
		print('\n' + WAIT + '\033[38;5;51mWriting function files \033[38;5;15m...')
		init = init + 1
		print('\t' + WAIT + 'Writing cd\'s function file ...', end='')
		install.installaddons(addons.functions.cd, DX2FUNCS, 'cd.func')
		print('\r\t' + DONE)
		print('\033[' + str(init + 1) + 'A\r' + DONE + '\033[' + str(init) + 'B')
		"""
			FOURTH SUB
		"""
#		init = 0
		print('\n' + WAIT + '\033[38;5;51mSetting permission for executable scripts \033[38;5;15m...')
		install.chmodbinfiles()
		print('\n')
#	def advancedinstall():
#		

class addons:
	class bin:
		webserver = (r"""#!/bin/bash

echo -e "\nStart HTTP server and serve files from \033[00;01;36m$PWD\033[m?"
echo -e -n "\033[00;01m[\033[32mY\033[00;01m/\033[38;5;196mn\033[00;01m]\033[m: "
read
case $REPLY in
	'y'|'Y'|'')
		echo -e "\nStarting HTTP Server...\n\nHit \033[00;01;38;5;196m[\033[00;01mCTRL\033[00;01;38;5;196m]\033[00;01m + \033[00;01;38;5;196m[\033[00;01mc\033[00;01;38;5;196m]\033[00;01m to stop.\n"
		python -m SimpleHTTPServer
		;;
	'n'|'N')
		return
		;;
	*)
		echo -e "Invalid key"
		;;
esac#!/bin/bash

echo -e "\033c\n  Do you want to start a web server & serve\n  the files from this dir (\033[00;01;36m$PWD\033[m)?\n"
echo -e -n "  \033[00;01m[\033[32mY\033[00;01m/\033[38;5;196mn\033[00;01m]\033[m: "
read
case $REPLY in
	'y'|'Y'|'')
		echo -e "\033c\n  Starting HTTP Server...\n\n  Hit \033[00;01;38;5;196m[\033[00;01mCTRL\033[00;01;38;5;196m]\033[00;01m + \033[00;01;38;5;196m[\033[00;01mc\033[00;01;38;5;196m]\033[00;01m to stop.\n"
		python -m SimpleHTTPServer
		;;
	'n'|'N')
		return
		;;
	*)
		echo -e "Invalid key"
		;;
esac
""")
		colormap = (r"""#!/usr/bin/env python3

import sys, os

_VERSION_ = "1.0"

initcount = 0

def cmap():
	print('[00;01mBasic Colors: [m')
	initcount = 0
	count = 7
	while count >= 0:
		print('[m' + str(initcount).zfill(2) + ':[38;5;16;4;48;5;' + str(initcount) + 'm  [m ',end='')
		initcount += 1
		count -= 1
	print('')
	count = 7
	while count >= 0:
		print('[m' + str(initcount).zfill(2) + ':[38;5;16;4;48;5;' + str(initcount) + 'm  [m ',end='')
		initcount += 1
		count -= 1
	print('')
	print('')
	print('[00;01mAdvanced colors: [m')
	initcount = 16
	while initcount < 232:
		countb = 6
		while countb > 0:
			count = 6
			while count > 0:
				print('[m' + str(initcount).zfill(3) + ':[38;5;16;4;48;5;' + str(initcount) + 'm   [m ',end='')
				initcount += 1
				count -= 1
			countb -= 1
			print('')
		print('')
	print('[00;01mShades of grey: [m')
	while initcount < 256:
		count = 6
		while count > 0:
			print('[m   ' + '[' + str(len(str(initcount))) + 'D' + str(initcount) + ':[38;5;16;4;48;5;' + str(initcount) + 'm   [m ',end='')
			initcount += 1
			count -= 1
		print('')


cmap()
""")
	class functions:
		cd = (r"""function cd(){
	builtin cd $*
	LC_COLLATE='C' \ls --color=always --group-directories-first -ALF -w $COLUMNS
	echo
}
""")
	class aliases:
		ls = (r"""export LS_ARG="--color=always --group-directories-first -F"

alias {l,ls}="\ls $LS_ARG -L"
alias {L,LS}="\ls $LS_ARG"
alias LS="\ls $LS_ARG"
alias ll="ls -l"
alias la="ls -A"
""")
		git = (r"""alias gs="git status"
alias gpm="git push -u origin master"
alias gpull="git pull"
alias gcom="git commit -m"
alias gco="git checkout"
alias gcob="git checkout -b"
""")
		misc = (r"""alias lg=lazygit
#alias webserver="python -m SimpleHTTPServer"
""")
		colormap = (r"""alias colormap="colormap | \less -er -P '[46m[38;5;16m  -- [47mHit [42m[[47mPGDN[42m][[47mPGUP[42m][47m to scroll or [41m[[47mQ[41m][47m to quit [46m--[m'"
""")

def asktoinstall():
	print('\033c\n\n  Do you want to install all the addons ?\n\n  [Y/n]', end='')
	installyn = input(': ')
	print('\033c\n')
	if installyn == 'Y':
		print('\033[00;01;38;5;196m Ａｕｔｏｍａｔｉｃａｌｌｙ  Ｉｎｓｔａｌｌｉｎｇ  Ａｄｄ－ｏｎ  Ｆｉｌｅｓ \033[38;5;15m...')
		install.automatic()
		print('\r  ' + DONE + '\n')
	elif installyn == 'y':
		print('\033[00;01;38;5;196m Automatically installing all add-on filesＡｕｔｏｍａｔｉｃａｌｌｙ  Ｉｎｓｔａｌｌｉｎｇ  Ａｄｄ－ｏｎ  Ｆｉｌｅｓ \033[38;5;15m...')
#		print('Automatically installing all add-on files ...')
		install.automatic()
		print('\r  ' + DONE + '\n')
	elif installyn == '':
		print('\033[00;01;38;5;196m Ａｕｔｏｍａｔｉｃａｌｌｙ  Ｉｎｓｔａｌｌｉｎｇ  Ａｄｄ－ｏｎ  Ｆｉｌｅｓ \033[38;5;15m...')
#		print('Automatically installing all add-on files ...')
		install.automatic()
#		print('\r  ' + DONE + '\n')
	elif installyn == 'n':
		print('\n  Exiting ...\n')
		return
	elif installyn == 'N':
		print('\n  Exiting ...\n')
		exit
	else:
		print('Invalid selection')
		exit



#install.installaddons(addons.aliases.ls, (DX2AKA + '/ls.aka'), 'n')
#install.automatic()
#titlebar('SetupDX2 - Addons Install')
#options('1', 'Testing', '51')
#options('2', 'Testing', '51')

asktoinstall()


